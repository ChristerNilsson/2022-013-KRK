#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SetupUtils

# def main():
#     # Initial setup to gather test_mode and n
#     test_mode, n = SetupUtils.begin_setup()
#
#     # Set up for test mode
#     if test_mode:
#         SetupUtils.test_mode_setup(n)
#     # Set up for competition mode
#     else:
#         SetupUtils.competition_setup(n)
#
#     restart_str = input('Would you like to play again? (y/n) >> ').upper() # raw
#     while restart_str not in ['Y','YES','N','NO']:
#         print('%s is not a valid response.' % restart_str)
#         restart_str = input('Would you like to play again? (y/n) >> ').upper() # raw
#
#     if restart_str in ['Y','YES']:
#         main()
#     else:
#         exit(0)

def main():
    n = 35
    SetupUtils.test_mode_setup(n)

if __name__ == '__main__':
    main()
