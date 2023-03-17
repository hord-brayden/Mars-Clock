# Mars-Clock
Deriviative, but functional JPL Martian Clock


Here's a description of the values used in the _calculate_mars_sol_date() function:

self.julian_date: This is the Julian date of the UTC time, which is calculated in the _calculate_julian_date() method. The Julian date is the number of days that have elapsed since January 1, 4713 BCE (Julian calendar).

2451549.5: This is the Julian date of January 1, 2000, which is the epoch used by NASA to calculate Martian time.

1.027491252: This is the length of a Martian solar day in Earth days. This means that a day on Mars is about 2.7% longer than a day on Earth.

44796.0: This is the offset in Martian solar days between the Julian date of January 1, 2000 and the first day of the Viking 1 mission on Mars, which landed on July 20, 1976. This offset is added to the result of the calculation to ensure that the Martian sol date starts from a known point.

0.00096: This is a correction factor that takes into account the variation in the length of a Martian day due to the eccentricity of Mars' orbit. This factor is subtracted from the result of the calculation to adjust for this variation.

The _calculate_mars_sol_date() function takes the Julian date of the UTC time and calculates the corresponding Martian sol date based on the length of a Martian solar day and the offset between the Julian date of January 1, 2000 and the first day of the Viking 1 mission. The resulting Martian sol date is then adjusted by a correction factor to account for the variation in the length of a Martian day. The final result is the number of Martian solar days that have elapsed since the start of the Viking 1 mission.
