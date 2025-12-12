# Masters of the Universe Coding Assignment

As a business user I need a tool that reads an accounting log in csv format that sums up all amounts per account_id and month and outputs a csv with summaries so we can double check the bookings easily.

## Acceptance Criteria
* the tool accepts 2 file names (input and output)
* output is a csv file with following fields
  * MONTH - the month of the booking in format yyyy-mm
  * ACCOUNT_ID - an ACCOUNT_ID from the input file
  * SUM_OF_AMOUNT - the sum of all input amounts for a ACCOUNT_ID per MONTH
* empty lines in the input file are ignored
* the amount from the input is summed up, grouped by ACCOUNT_ID and MONTH

## Format for the input csv
  * separator is a comma ','
  * the file has a header line
  * there are no quotes used
  * there can't be a comma in one of the fields
  * the file may contain empty lines (no character or just white spaces)
  * the file is encoded in UTF-8 without BOM marker
  * the file has 4 columns
    * TIME_STAMP - time of booking in format yyyy-mm-dd hh:mi:ss
    * ACCOUNT_ID - Integer number
    * EMPLOYEE - String (name of employee)
    * AMOUNT - floating point number
  * the Output should have a heder line (MONTH,ACCOUNT_ID,AMOUNT)
## Sample files:
* good_input.csv - a sample input file that has no validation error
* good_output.csv - expected output from processing good_input.csv

## Nice to have
* the tool writes a error file with rejected records
* the header and each line is checked for the expected number of columns
* every field is trimmed from whitespace
* input record validation is done
  * no field may be empty after trimming
  * TIME_STAMP must be in expected format
  * only valid ACCOUNT_ID are accepted, list of IDs:
    * 10101
    * 10302
    * 10506
    * 10780
* input lines that are rejected in validation are written to an error csv file
* the error records have an additional column with a reason for being rejected

## Sample files for 'Nice to have':
* input_with_error.csv - a sample input file that has all kinds of validation problems
* input_with_error_output.csv - expected output from processing input_with_error.csv
