#!/usr/bin/env python3

from decimal import Decimal, ROUND_HALF_UP


def main():

    # Sample marks in each CA component
    labs = 100
    bucket_list = 90
    labexam_01 = 73
    labexam_02 = 90

    ca = (1 * labs) + (2 * bucket_list) + (3 * labexam_01) + (4 * labexam_02)
    ca = ca / 10

    # Round to nearest integer (with .5 always rounding up)
    ca = int(Decimal(ca).to_integral_value(ROUND_HALF_UP))

    print('Your overall CA mark is: {:d}%'.format(ca))


if __name__ == "__main__":
    main()
