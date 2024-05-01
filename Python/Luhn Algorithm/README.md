# Luhn Algorithm

The Luhn Algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, and Canadian Social Insurance Numbers. It is named after its creator, Hans Peter Luhn, a computer scientist who formulated the algorithm in the 1960s.

## Overview

This repository contains an implementation of the Luhn Algorithm in various programming languages. The algorithm works by performing the following steps on a given identification number:

1. Starting from the rightmost digit, double every other digit.
2. If the result of doubling a digit is greater than 9, subtract 9 from the result.
3. Sum all the digits.
4. If the sum is divisible by 10, the identification number is valid.

The repository includes implementations of the Luhn Algorithm in multiple programming languages, allowing you to compare and learn different approaches to solving the same problem.
