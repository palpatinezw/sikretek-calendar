# Usage

`adv` (`a`) - Advances the current date by some number of days
* `out` - takes `en`, `sk`, `en-sh`, `en-sk` values - outputs the date advanced to the output file 
* `value` - advances the number of days indicated in value (defaults to 1)

`bck` (`b`) - Backtracks the current date by 1 day
* `out` - takes `en`, `sk`, `en-sh`, `en-sk` values - outputs the date advanced to the output file 
* `value` - advances the number of days indicated in value (defaults to 1)

`tdy` - Sets the working date to the current date

`str` - Gets the full string representation of the current date

`goto` - Goes to a specified date
* `target` - The date to go to, in the format YYYY-MM-DD

`end` (`q`) - Stops the current program

# Output forms
## Natlang forms

## Shorthand forms
### English shorthand `en-sh`
Presented in the format `DD-MMX-YYYR`. 

`DD` represents the day. It is either a number between `01` and `14` representing the numerical date, `ML` representing the Moon of Light (full moon), `MD` representing the Moon of Darkness (new moon), `DL` representing the Day of Light (summer solstice), or `DD` representing the Day of Darkness (winter solstice). 

`MM` represents the month. It is either a number between `01` and `12` representing the numerical month, `LL` representing the Moon of the Day of Light, `GL` representing the Grand Moon, or `DD` representing the Moon of the Day of Darkness.

`X` represents the submonth. It is either `F` for the falling moon, `R` for the rising moon, `L` for the Moon of Light (full moon), or `D` for the Moon of Darkness (new moon).

`YYYR` represents the year, given as 2 numbers followed by `AR` for After Revelation, or `BR` for Before Revelation

### Sikretek shorthand `sk-sh`
Presented in the format `DD-MMX-YYYyyN`. 

`DD` represents the day. It is either a number between `01` and `14` representing the numerical date, `SK` representing the Sihèrokenol (full moon), `HK` representing the Heisèrikenol (new moon), `SJ` representing the Sihèrojoru (summer solstice), or `HJ` representing the Heisèrijoru (winter solstice). 

`MM` represents the month. It is either a number between `01` and `12` representing the numerical month, `SJ` representing the Kanol Sihèrojorum, `KA` representing the Kai Kanol, or `HJ` representing the Kanol Heisèrijorum.

`X` represents the submonth. It is either `T` for the Teimikenol, `M` for the Makunikenol, `S` for the Sihèrokenol (full moon), or `H` for the Heisèrikenol (new moon).

`YYYyyN` represents the year, given as 2 numbers followed by `KoiR` for Koilo Ritriuy, or `KeiR` for Keili Ritriuy