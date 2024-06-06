#!/usr/bin/env python3

import re
import sys
from traceback import print_exc
from codecs import escape_decode
from pyhdbpp import reader, get_default_reader
from pyhdbpp.utils import is_regexp, export_to_text, str2time, time2str, date2time
from os.path import exists
from collections.abc import Sequence

from fandango.dicts import SortedDict
from fandango.tango import get_full_name

__doc__ = """
Script to extract values from archiving databases

Usage:

 hdb2csv [--options] attribute1 attribute2 date1 date2 /.../filename.cvs

  attributes should be in domain/family/member/attribute format
  dates should be specified in quoted "Y-m-d H:M" format
  filename should include path

 Available options for extraction are:

  --schema="database" : choose database to extract the data
  --arrsep=""/--no-sep : default separator between arrays values
  --sep : separator between columns
  --linesep : character between lines
  --resolution=X(s) : force periodicity of values to a fix period
  --list : list available schemas for attributes
  --nofill : do not fill gaps using last values
  --noheader : do not include headers
  --nodate : do not include datetime
  --noepoch : do not include epochs
"""


def is_filename(a):
    return (not is_regexp(a)
            and ('/' not in a or exists(a.rsplit('/', 1)[0])))


def report_values(values):
    print(' \n'.join(sorted('{}: {} values between {} and {} '
                            .format(a, len(v), time2str(v[0][0]),
                                    time2str(v[-1][0]))
                            for a, v in values.items() if v)))


def main(*args):
    sep = '\t'
    linesep = '\n'
    arrsep = ', '
    lines = []
    filename = ''
    nofill = False

    # PARSING ARGS ###########################################################

    try:
        args = args if len(args) else sys.argv[1:]

        if not args or any(a in args
                           for a in ('-?', '-h', '--help', 'help')):
            print(__doc__)
            sys.exit(0)

        attrs = [a for a in args if not a.startswith('-')]
        args = [a for a in args if a.startswith('-')]

        if attrs and is_filename(attrs[-1]):
            filename = attrs.pop(-1)

        if '--list' in args:
            pass

        elif attrs:
            # assert filename and len(attrs)>3, "Dates and filename required!"
            start, stop = attrs[-2:]
            attrs = list(map(str.lower, attrs[:-2]))
            assert str2time(start) > 0, 'wrong start value'
            assert str2time(stop) > 0, 'wrong stop value'
            assert [a.split('/')[2] for a in attrs]  # will fail if wrong format

        if attrs:
            ext = [a for a in attrs if is_regexp(a)]
            if ext:
                [attrs.remove(e) for e in ext]
                rd = get_default_reader()
                for a in rd.get_attributes():
                    if any(re.match("*{}".format(e), a, flags=re.IGNORECASE)
                           for e in ext):
                        attrs.append(a)

            attrs = [get_full_name(a, fqdn=1).lower() for a in attrs]

        schema = '*'
        for a in args[:]:
            if a.startswith('--schema='):
                schema = a.split('=')[-1]
                args.remove(a)

    except:
        print_exc()
        print('\nWrong arguments, right syntax is:\n\t')
        print(__doc__)
        sys.exit(-1)

    if "--list" in args:
        if schema in ["*"]:
            rd = get_default_reader()
            print("Using default reader with schemas {}"
                  .format(list(rd.attributes.keys())))
        else:
            rd = reader(config=schema)
            print("Using {} schema".format(schema))

        print("Listing attributes for {}".format(schema))
        print(rd.get_attributes())

    # EXTRACT VALUES ###########################################################

    else:
        # Getting the right Reader object
        if schema in ["*"]:
            rd = get_default_reader()
            print("Using default reader with schemas {}"
                  .format(list(rd.attributes.keys())))
        else:
            rd = reader(config=schema)
            print("Using {} schema".format(schema))

        print('hdb2csv: Attributes: {}\nStart: {}\nStop: {}\n'
              .format(attrs, start, stop))
        correlate = len(attrs) > 1
        for a in args:
            if a.startswith('--resolution='):
                correlate = float(a.replace('--resolution=', ''))
                print(
                    'hdb2csv: Correlation step set to {} s'.format(correlate))
            if a.startswith('--arrsep='):
                arrsep = a.split('=', 1)[-1]
                arrsep = escape_decode(arrsep)[0]
            if a.startswith('--sep='):
                sep = a.split('=', 1)[-1]
                sep = escape_decode(sep)[0]
            if a.startswith('--linesep='):
                linesep = a.split('=', 1)[-1]
                linesep = escape_decode(linesep)[0]
            if a == '--nosep':
                sep = arrsep = ' '
            if a == '--nofill':
                nofill = True

        Ts = str2time(start), str2time(stop)

        raws = rd.get_attributes_values(attrs, start, stop, text=False,
                                        decimate=correlate, correlate=False,
                                        lasts=True)
        values = SortedDict()
        for a in attrs:
            try:
                values[a] = raws[a]
            except KeyError:
                print("Warning: attribute {} cannot be retrieved at schema {}"
					   .format(a, schema))

        print('hdb2csv({},{})'.format(start, stop))
        print('hdb2csv: Obtained data from database:')
        report_values(values)
        ll = max(len(v) for v in values.values()) - 1

        if correlate:
            print('hdb2csv: Filtering {} arrays (1/{}T)'.format(
                len(values), correlate))
            if nofill:
                print('--nofill')

            import fandango
            for a, v in values.items():
                if len(v) == 0:
                    lval = rd.get_last_attribute_value(a, time_bound=start)[0]
                    print((date2time(lval[0]), lval[1], lval[2]))
                    v.append((date2time(lval[0]), lval[1], lval[2]))
                    print("Appended last value known before date")
                print('{} [{}] : {}'.format(a, len(v),
                                            '{}...{}'.format(v[0],
                                                             v[-1]) if len(
                                                v) else '...'))
            for a, v in values.items():
                try:
                    is_array = False
                    for vv in v:
                        if vv[1] is not None:
                            if (not isinstance(vv[1], (str, bytes))
                                    and isinstance(vv[1], Sequence)):
                                is_array = True
                            else:
                                break
                    tt = (Ts[-1] + (correlate or 1), v[-1][1])
                    tt = type(v[-1])(tt)  # Type matters when sorting!
                    v.append(tt)
                    if is_array:
                        values[a] = []
                        for t, vv in v:
                            if not values[a]:
                                values[a].append(
                                    (t, vv))  # TODO: should be rounded
                            # fill up output until catching the raw values
                            while values[a][-1][0] + correlate < t:
                                values[a].append(
                                    (values[a][-1][0] + correlate, vv))
                            # this inserts into original only if a value matches?
                            # TODO: what happens if no value matches!?!?!
                            # TODO: int(t) should be rounded!!!
                            if int(t) == int(values[a][-1][0]) + correlate:
                                values[a].append((t, vv))
                    else:
                        values[a] = fandango.arrays.filter_array(
                            v, window=correlate,
                            filling=fandango.arrays.F_ZERO if nofill
                            else fandango.arrays.F_LAST,
                            # begin=int(Ts[0]),
                            # end=int(Ts[1]),
                            trace=True,
                        )
                        print(a, values[a][0], values[a][-1])

                except Exception as e:
                    print_exc()
                    print(
                        'Unable to correlate {} data, please try to export it '
                        'to a separate file'.format(a))
                    values.pop(a)

            if not values:
                print('hdb2csv: Unable to export data ...')
                sys.exit()

            # if len(attrs)>1:
            try:
                # Ts = (max(v[0][0] for v in values.values()),
                # min(v[-1][0] for v in values.values()))
                print(
                    'interval: {} : {}'.format(str(Ts),
                                               map(fandango.time2str, Ts)))
                for a, v in values.items():
                    l = len(v)
                    values[a] = [t for t in v if Ts[0] <= t[0] <= Ts[-1]]
                    dl = l - len(values[a])
                    if dl:
                        print('{}: removed {} values out of interval'.format(a,
                                                                             dl))

            except Exception:
                print_exc()

            report_values(values)

        options = {'arrsep': arrsep, 'sep': sep, 'linesep': linesep}
        print('hdb2csv: Options: {}'.format(options))
        data = export_to_text(
            values, order=attrs, **options).replace('None', 'NaN')

        # Remove repeated dates
        lines = data.split(linesep)
        ll = i = len(lines) - 1
        while i:
            # if lines[i].split('\t')[1]==lines[i-1].split('\t')[1]:
            if lines[i] == lines[i - 1]:
                lines.pop(i - 1)
            i -= 1
        # print('data reduction: {} -> {}'.format(ll,len(lines)))

        skip = 0 if '--nodate' in args else (1 if '--noepoch' in args else None)
        if skip is not None:
            for i, l in enumerate(lines):
                l = l.split(sep)
                try:
                    l.pop(skip)
                    lines[i] = sep.join(l)
                except:
                    print(i, l, '?')

        if '--noheader' in args:
            lines = lines[1:]

    # SAVING FILE ###########################################################

    if filename:
        print('hdb2csv: Writing {}'.format(filename))
        data = linesep.join(lines)
        open(filename, 'w').write(data)

    else:
        for line in lines:
            print(str(line))


if __name__ == '__main__':
    main(*sys.argv[1:])
