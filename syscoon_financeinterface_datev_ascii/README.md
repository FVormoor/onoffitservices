# Changelog

## 15.0.0.0.33

- Improve serach for datev_ref when partially paid

## 15.0.0.0.32

- change from action_post to _post for overall checks and generation of BEDI

## 15.0.0.0.31

- prevent thorwing error if no Buchungstext is configured

## 15.0.0.0.30

- fix problems with bedi beleglink

## 15.0.0.0.29

- make datev_ref searcheable

## 15.0.0.0.28

- Add country code to Land because of OSS

## 15.0.0.0.27

- replace line_count in datev checks with line name

## 15.0.0.0.26

- solve little issues with tests

## 15.0.0.0.25

- Change function calculate differences when foreign currecny is used
- Change function to skip tax move lines

## 15.0.0.0.24

- ValueError: Expected singleton: account.move

## 15.0.0.0.23

- UnboundLocalError: local variable 'line' referenced before assignment

## 15.0.0.0.22

- change bookingtext to line.name instead of line.label

## 15.0.0.0.21

- solve problem with wrong created datev_bedi
- do post migration of the datev_bedi (will change all records where datev_bedi = True)

## 15.0.0.0.20

- solve error if line.move_id.invoice_date is bool

## 15.0.0.0.19

- Add Leistungsdatum if it differs from Belegdatum

## 15.0.0.0.18

- de.po translation update

## 15.0.0.0.17

- extend search for account_asset module by state

## 15.0.0.0.16

- remove outcomment of payment id in payment term for DATEV

## 15.0.0.0.15

- Adding guid (uuid5) for BEDI Beleglink to ASCII file for preparation of online API.

## 15.0.0.0.14

- Remove constraint at datev_payment_term_id

## 15.0.0.0.13

- Better handling of balancing move total amount

## 15.0.0.0.12

- Fix wrong behavoir with booking text configuration

## 15.0.0.0.11

- Solve rounding problem - it was added if amount was negativ

## 15.0.0.0.10

- Add sudo to search in some cases, because of access restrictions

## 15.0.0.0.9

- Replace self.env.user.company id by self.env.company

## 15.0.0.0.8

- Move grouping export lines from config to account journal and little changes in
  function of it
- Add journal to bookingtext configuration
