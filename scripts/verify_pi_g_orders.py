#!/usr/bin/env python3
"""Verify the polygonal N-Series order table in the Ramanujan comparison note."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import mpmath as mp

N_VALUES = (32,64,128,256,512,1024)

def raw(n: int) -> mp.mpf:
    return mp.mpf(n) * mp.sin(mp.pi / n)

def two_scale(n: int) -> mp.mpf:
    return (4*raw(2*n)-raw(n))/3

def three_scale(n: int) -> mp.mpf:
    return raw(n)/45 - 4*raw(2*n)/9 + 64*raw(4*n)/45

def order_at_displayed_scale(fn, n: int) -> mp.mpf:
    e_prev = abs(fn(n//2)-mp.pi)
    e_now = abs(fn(n)-mp.pi)
    return mp.log(e_prev/e_now, 2)

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--precision',type=int,default=100)
    parser.add_argument('--output-dir',type=Path,default=Path('output'))
    args=parser.parse_args()
    if args.precision < 60:
        raise ValueError('Use at least 60 decimal digits.')
    mp.mp.dps=args.precision
    rows=[]
    for n in N_VALUES:
        rows.append({
            'N':n,
            'raw_order':mp.nstr(order_at_displayed_scale(raw,n),18),
            'two_scale_order':mp.nstr(order_at_displayed_scale(two_scale,n),18),
            'three_scale_order':mp.nstr(order_at_displayed_scale(three_scale,n),18),
            'raw_abs_error':mp.nstr(abs(raw(n)-mp.pi),30),
            'two_scale_abs_error':mp.nstr(abs(two_scale(n)-mp.pi),30),
            'three_scale_abs_error':mp.nstr(abs(three_scale(n)-mp.pi),30),
        })
    args.output_dir.mkdir(parents=True,exist_ok=True)
    with (args.output_dir/'pi_g_order_results.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    expected_orders = {
        32: ('1.99791411','3.99875845','5.99923958'),
        64: ('1.99947855','3.99968962','5.99980989'),
        128:('1.99986964','3.99992240','5.99995247'),
        256:('1.99996741','3.99998060','5.99998812'),
        512:('1.99999185','3.99999515','5.99999703'),
        1024:('1.99999796','3.99999879','5.99999926'),
    }
    table_pass=True
    for row in rows:
        n=row['N']
        got=(mp.mpf(row['raw_order']),mp.mpf(row['two_scale_order']),mp.mpf(row['three_scale_order']))
        exp=tuple(mp.mpf(x) for x in expected_orders[n])
        table_pass &= all(abs(a-b)<mp.mpf('5e-9') for a,b in zip(got,exp))

    last=rows[-1]
    expected_errors=(
        mp.mpf('4.92831263353783379e-6'),
        mp.mpf('5.79840008299119192e-13'),
        mp.mpf('8.12154741379365833e-21'),
    )
    got_errors=tuple(mp.mpf(last[k]) for k in ('raw_abs_error','two_scale_abs_error','three_scale_abs_error'))
    error_pass=all(abs(a-b)<=mp.mpf('1e-17')*max(abs(b),mp.mpf('1e-30')) for a,b in zip(got_errors,expected_errors))
    convergence_pass=(
        abs(mp.mpf(last['raw_order'])-2)<mp.mpf('3e-6') and
        abs(mp.mpf(last['two_scale_order'])-4)<mp.mpf('2e-6') and
        abs(mp.mpf(last['three_scale_order'])-6)<mp.mpf('1e-6')
    )
    overall=bool(table_pass and error_pass and convergence_pass)
    summary={
        'precision_dps':args.precision,
        'displayed_scales':list(N_VALUES),
        'order_definition':'log2(error at N/2 divided by error at N)',
        'table_values_passed':bool(table_pass),
        'N1024_errors_passed':bool(error_pass),
        'orders_converge_to_2_4_6':bool(convergence_pass),
        'verification_passed':overall,
    }
    (args.output_dir/'pi_g_order_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    (args.output_dir/'pi_g_order_summary.txt').write_text('\n'.join(f'{k}: {v}' for k,v in summary.items())+'\n',encoding='utf-8')
    print('\n'.join(f'{k}: {v}' for k,v in summary.items()))
    if not overall: raise SystemExit('Verification failed.')

if __name__=='__main__': main()
