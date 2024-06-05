Model Parameters
================

Excel input file parameter description
--------------------------------------

The table below displays the input parameters of RAMP. If NA is
displayed in the table below, it means that the corresponding column is
not applicable to the parameter.

When filling .xlsx input file, you can simply leave the cell empty if
the parameter is not mandatory and the default value will be
automatically used.

The “allowed values” column provide information about the format one
should provide when:

-  {1,2,3} is a set and the allowed value are either 1, 2 or 3;
-  in [0-1440] is a range and the allowed value must lie between 0 and
   1440. 0 and 1440 are also possible values.

+-----+---+---+------------------------------------------------+---+----+---+
| Nam | U | A | Description                                    | C | Is | D |
| e   | n | l |                                                | o | th | e |
|     | i | l |                                                | d | is | f |
|     | t | o |                                                | i | va | a |
|     |   | w |                                                | n | lu | u |
|     |   | e |                                                | g | e  | l |
|     |   | d |                                                | t | ma | t |
|     |   | v |                                                | y | nd | v |
|     |   | a |                                                | p | at | a |
|     |   | l |                                                | e | or | l |
|     |   | u |                                                |   | y? | u |
|     |   | e |                                                |   |    | e |
|     |   | s |                                                |   |    |   |
+=====+===+===+================================================+===+====+===+
| use | N | N | Name of user type                              | s | ye | N |
| r_n | A | A |                                                | t | s  | A |
| ame |   |   |                                                | r |    |   |
|     |   |   |                                                | i |    |   |
|     |   |   |                                                | n |    |   |
|     |   |   |                                                | g |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| num | N | > | Number of users within the resprective         | i | ye | 0 |
| _us | A | = | user-type                                      | n | s  |   |
| ers |   | 0 |                                                | t |    |   |
|     |   |   |                                                | e |    |   |
|     |   |   |                                                | g |    |   |
|     |   |   |                                                | e |    |   |
|     |   |   |                                                | r |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| use | N | { | Related to cooking behaviour, how many types   | i | no | 0 |
| r_p | A | 0 | of meal a user wants a day (number of user     | n |    |   |
| ref |   | , | preferences has to be defined here and will be | t |    |   |
| ere |   | 1 | further specified with pref_index parameter)   | e |    |   |
| nce |   | , |                                                | g |    |   |
|     |   | 2 |                                                | e |    |   |
|     |   | , |                                                | r |    |   |
|     |   | 3 |                                                |   |    |   |
|     |   | } |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| nam | N | N | Appliance name                                 | s | ye | N |
| e   | A | A |                                                | t | s  | A |
|     |   |   |                                                | r |    |   |
|     |   |   |                                                | i |    |   |
|     |   |   |                                                | n |    |   |
|     |   |   |                                                | g |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| num | N | > | Number of appliances                           | i | ye | 0 |
| ber | A | = |                                                | n | s  |   |
|     |   | 0 |                                                | t |    |   |
|     |   |   |                                                | e |    |   |
|     |   |   |                                                | g |    |   |
|     |   |   |                                                | e |    |   |
|     |   |   |                                                | r |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| pow | W | > | Power rating of appliance (average)            | F | ye | 0 |
| er  | a | = |                                                | l | s  |   |
|     | t | 0 |                                                | o |    |   |
|     | t |   |                                                | a |    |   |
|     |   |   |                                                | t |    |   |
|     |   |   |                                                | o |    |   |
|     |   |   |                                                | r |    |   |
|     |   |   |                                                | a |    |   |
|     |   |   |                                                | r |    |   |
|     |   |   |                                                | r |    |   |
|     |   |   |                                                | a |    |   |
|     |   |   |                                                | y |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| num | N | { | Number of distinct time windows, e.g. if an    | i | ye | 1 |
| _wi | A | 1 | appliance is running 24 h the num_windows is   | n | s  |   |
| ndo |   | , | 1. If num_windows is set to x then you have to | t |    |   |
| ws  |   | 2 | fill in the window_x_start, window_x_end and   | e |    |   |
|     |   | , | random_var_w parameters)                       | g |    |   |
|     |   | 3 |                                                | e |    |   |
|     |   | } |                                                | r |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| fun | m | i | Total time an appliance is running in a day    | i | ye | 0 |
| c_t | i | n | (not dependant on windows)                     | n | s  |   |
| ime | n | [ |                                                | t |    |   |
|     | u | 0 |                                                | e |    |   |
|     | t | , |                                                | g |    |   |
|     | e | 1 |                                                | e |    |   |
|     | s | 4 |                                                | r |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| tim | % | i | For time (not for windows), randomizes the     | f | no | 0 |
| e_f |   | n | total time the appliance is on                 | l |    |   |
| rac |   | [ |                                                | o |    |   |
| tio |   | 0 |                                                | a |    |   |
| n_r |   | , |                                                | t |    |   |
| and |   | 1 |                                                |   |    |   |
| om_ |   | ] |                                                |   |    |   |
| var |   |   |                                                |   |    |   |
| iab |   |   |                                                |   |    |   |
| ili |   |   |                                                |   |    |   |
| ty  |   |   |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| fun | m | i | Running time: time the appliance is on (after  | f | ye | 1 |
| c_c | i | n | switching it on)                               | l | s  |   |
| ycl | n | [ |                                                | o |    |   |
| e   | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| fix | N | { | All appliances of the same kind (e.g. street   | b | no | n |
| ed  | A | y | lights) are switched on at the same time (if   | o |    | o |
|     |   | e | fixed=yes)                                     | o |    |   |
|     |   | s |                                                | l |    |   |
|     |   | , |                                                | e |    |   |
|     |   | n |                                                | a |    |   |
|     |   | o |                                                | n |    |   |
|     |   | } |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| fix | N | { | Number of duty cycle, 0 means continuous       | i | no | 0 |
| ed_ | A | 0 | power, if not 0 you have to fill the cw (cycle | n |    |   |
| cyc |   | , | window) parameter (you may define up to 3 cws) | t |    |   |
| le  |   | 1 |                                                | e |    |   |
|     |   | , |                                                | g |    |   |
|     |   | 2 |                                                | e |    |   |
|     |   | , |                                                | r |    |   |
|     |   | 3 |                                                |   |    |   |
|     |   | } |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| occ | % | i | Defines how often the appliance is used,       | f | no | 1 |
| asi |   | n | e.g. every second day will be 0.5              | l |    |   |
| ona |   | [ |                                                | o |    |   |
| l_u |   | 0 |                                                | a |    |   |
| se  |   | , |                                                | t |    |   |
|     |   | 1 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| fla | N | { | no variability in the time of usage, similar   | b | no | n |
| t   | A | y | to fixed, but does not account for all         | o |    | o |
|     |   | e | appliances of the same type at the same time,  | o |    |   |
|     |   | s | no, if switched on and off at different times  | l |    |   |
|     |   | , | for different days                             | e |    |   |
|     |   | n |                                                | a |    |   |
|     |   | o |                                                | n |    |   |
|     |   | } |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| the | % | i | Range of change of the power of the appliance  | f | no | 0 |
| rma |   | n | (e.g. shower not taken at same temparature) or | l |    |   |
| l_p |   | [ | for the power of duty cycles (e.g. for a       | o |    |   |
| _va |   | 0 | cooker, AC, heater if external temperature is  | a |    |   |
| r   |   | , | different…)                                    | t |    |   |
|     |   | 1 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| pre | N | { | This number must be smaller or equal to the    | i | no | 0 |
| f_i | A | 0 | value input in user_preference                 | n |    |   |
| nde |   | , |                                                | t |    |   |
| x   |   | 1 |                                                | e |    |   |
|     |   | , |                                                | g |    |   |
|     |   | 2 |                                                | e |    |   |
|     |   | , |                                                | r |    |   |
|     |   | 3 |                                                |   |    |   |
|     |   | } |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| wd_ | N | { | Specify whether the appliance is used only on  | i | no | 2 |
| we_ | A | 0 | weekdays (0), weekend (1) or the whole week    | n |    |   |
| typ |   | , | (2)                                            | t |    |   |
| e   |   | 1 |                                                | e |    |   |
|     |   | , |                                                | g |    |   |
|     |   | 2 |                                                | e |    |   |
|     |   | } |                                                | r |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| p_i | W | > | Power rating for first part of ith duty cycle. | f | no | 0 |
| 1   | a | = | Only necessary if fixed_cycle is set to I or   | l |    |   |
|     | t | 0 | greater                                        | o |    |   |
|     | t |   |                                                | a |    |   |
|     |   |   |                                                | t |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| t_i | m | i | Duration of first part of ith duty cycle. Only | f | no | 0 |
| 1   | i | n | necessary if fixed_cycle is set to I or        | l |    |   |
|     | n | [ | greater                                        | o |    |   |
|     | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| cwi | m | i | Window start time for the first part of ith    | f | no | 0 |
| 1_s | i | n | specific duty cycle number (not neccessarily   | l |    |   |
| tar | n | [ | linked to the overall time window)             | o |    |   |
| t   | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| cwi | m | i | Window end time for the first part of ith      | f | no | 0 |
| 1_e | i | n | specific duty cycle number (not neccessarily   | l |    |   |
| nd  | n | [ | linked to the overall time window)             | o |    |   |
|     | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| p_i | W | > | Power rating for second part of ith duty cycle | f | no | 0 |
| 2   | a | = | number. Only necessary if fixed_cycle is set   | l |    |   |
|     | t | 0 | to i or greater                                | o |    |   |
|     | t |   |                                                | a |    |   |
|     |   |   |                                                | t |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| t_i | m | i | Duration second part of ith duty cycle number. | f | no | 0 |
| 2   | i | n | Only necessary if fixed_cycle is set to I or   | l |    |   |
|     | n | [ | greater                                        | o |    |   |
|     | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| cwi | m | i | Window start time for the second part of ith   | f | no | 0 |
| 2_s | i | n | duty cycle number (not neccessarily linked to  | l |    |   |
| tar | n | [ | the overall time window)                       | o |    |   |
| t   | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| cwi | m | i | Window end time for the second part of ith     | f | no | 0 |
| 2_e | i | n | duty cycle number (not neccessarily linked to  | l |    |   |
| nd  | n | [ | the overall time window)                       | o |    |   |
|     | u | 0 |                                                | a |    |   |
|     | t | , |                                                | t |    |   |
|     | e | 1 |                                                |   |    |   |
|     | s | 4 |                                                |   |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| r_c | % | i | randomization of the duty cycle parts’         | f | no | 0 |
| i   |   | n | duration. There will be a uniform random       | l |    |   |
|     |   | [ | variation around t_i1 and t_i2. If this        | o |    |   |
|     |   | 0 | parameter is set to 0.1, then t_i1 and t_i2    | a |    |   |
|     |   | , | will be randomly reassigned between 90% and    | t |    |   |
|     |   | 1 | 110% of their initial value; 0 means no        |   |    |   |
|     |   | ] | randomisation                                  |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| win | m | i | Start time of time-window j. Only necessary if | i | ye | 0 |
| dow | i | n | num_windows is set to j or greater             | n | s  |   |
| _j_ | n | [ |                                                | t |    |   |
| sta | u | 0 |                                                | e |    |   |
| rt  | t | , |                                                | g |    |   |
|     | e | 1 |                                                | e |    |   |
|     | s | 4 |                                                | r |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| win | m | i | End time of time-window j. Only necessary if   | i | ye | 0 |
| dow | i | n | num_windows is set to j or greater             | n | s  |   |
| _j_ | n | [ |                                                | t |    |   |
| end | u | 0 |                                                | e |    |   |
|     | t | , |                                                | g |    |   |
|     | e | 1 |                                                | e |    |   |
|     | s | 4 |                                                | r |    |   |
|     |   | 4 |                                                |   |    |   |
|     |   | 0 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+
| ran | % | i | variability of the windows in percent, the     | f | no | 0 |
| dom |   | n | same for all windows                           | l |    |   |
| _va |   | [ |                                                | o |    |   |
| r_w |   | 0 |                                                | a |    |   |
|     |   | , |                                                | t |    |   |
|     |   | 1 |                                                |   |    |   |
|     |   | ] |                                                |   |    |   |
+-----+---+---+------------------------------------------------+---+----+---+

Python input file parameter description
---------------------------------------

A new instance of class ``User`` need the parameters ``user_name``,
``num_users``, ``user_preference`` from the table above. To add an
appliance use the method ``add_appliance`` with at least the mandatory
parameters listed in the table above (except the 3 first parameters
which belong to the user class and are already assigned in this case)
and with any of the non-mandatory ones.

If no window parameter (``window_j_start``, ``window_j_end``) is
provided to the ``add_appliance`` method of the user, then one must then
call the ``windows`` method of the appliance to provide up to 3 windows
: ``window_1``, ``window_2``, ``window_3`` as well as ``random_var_w``
The parameters to describe a window of time should simply directly be
provided as a numpy array ( for example
``window_j = np.array([window_j_start, window_j_end])``) (where j is an
integer smaller or equal to the provided value of ``num_windows``).

If no duty cycle parameter is provided to the ``add_appliance`` method
of the user, then one can then enable up to 3 duty cycle by calling the
method ``specific_cycle_i`` of the appliance (where i is an integer
smaller or equal to the provided value of ``fixed_cycle``) The
parameters to describe the ith duty cycle are the following: ``p_i1``,
``t_i1``, ``p_i2``, ``t_i2``, ``r_ci``, ``cwi1`` and ``cwi2`` It is also
possible to provide the parameters ``cwi1`` and ``cwi2`` using the
method ``cycle_behaviour`` of the appliance.

The legacy way to create an appliance instance is by using the
``Appliance`` method of the user (note that the names of input
parameters are the old ones). This way of creating an appliance is to
keep a back compatibility of the legacy input files, using the
``add_appliance`` method of the user should be preferred Note that with
the legacy way, one must then call the ``windows`` method of the
appliance to provide at least one windows. And one can add duty cycles
only via the method ``specific_cycle_i`` of the appliance.


:download:`Link to the jupyter notebook file </../notebooks/model_parameters.ipynb>`.
