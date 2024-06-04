#!/usr/bin/env python

import argparse
import FM14_transform.data2bufr as data2bufr
import os
import boto3

THISDIR = os.path.dirname(os.path.realpath(__file__))

def test():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def transform2bufr():
    parser = argparse.ArgumentParser(
        description='Utility to take as input a TAC or other text file containing a ' +
        'single FM14 SYNOP MOBIL record and convert to bufr file')
    parser.add_argument(
        'fm14', metavar='fm14', type=str, nargs=1,
        help='Filename of TAC or METAR bulletin'
    )

    parser.add_argument(
        'month', metavar='month', type=int, nargs=1,
        help='Numeric value (1-12) of the month of the observation'
    )
    parser.add_argument(
        'year', metavar='year', type=int, nargs=1,
        help='Year of the observation in YYYY format'
    )
    args = parser.parse_args()
    fm14_filename = args.fm14[0]
    month = args.month[0]
    year = args.year[0]
    # data = get_s3_objects()
    with open(fm14_filename) as fh:
        data = fh.read()
    results = data2bufr.transform(data, year, month)

    for item in results:
        print(item)
        bufr4 = item['bufr4']

def get_s3_objects():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='wis2-incoming', Key='test-FM14.txt')
    body = response["Body"].read().decode("utf-8")
    return body


    