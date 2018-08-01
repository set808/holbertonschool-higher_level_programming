#!/bin/bash
#Send POST request and display body of response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
