'''
=======================================================================================
=========================== Time Module in Python======================================
=======================================================================================
Time Module in python provide set of functions related to Time operations.




=======================================================================================
===> Epoch in python________________________________________________________________
=======================================================================================
The epoch is the moment when time begins for calculations in programs. 
The epoch is 1 January 1970, 00:00:00 (UTC) on Windows and most Unix systems, 
We can use time to find out what the epoch is on a particular platform.gmtime(0).





=======================================================================================
====================== Methods in Time Module =========================================
=======================================================================================

-> gmtime(0) :  It takes second passed since epoch and return struct time representation
-> time()    :  Returns the number of seconds passed since epoch (the point where time begins).
-> ctime()   : Takes (Seconds passed from epoch) and returns a string representation of local time.
-> sleep()   : Sleep or delay execution for seconds as in arguments
-> localtime() : It takes (seconds passed since epoch time) as Agrument and return tuple formate of current value
-> mktime()  : It converts struct time representation back into seconds passed since epoch time
-> asctime() : It takes struct representation as argument and return a string formate of time
'''

import time as T





'''
===============================================================================================
____________________________ Taking out seconds since epoch____________________________________
===============================================================================================
-> time()

(1) Using time() --> Return seconds passed since epoch
           output-->  1672197244.0
____________________________________________________________________________________________'''
print(f"\nSeconds Passed : {T.time()}")
# ____________________________________________________________________________________________









'''
===============================================================================================
______________________________|Seconds|  -->  |Struct_time|____________________________________
===============================================================================================
-> gmtime()
-> local time


Using gmtime(seconds) --> struct_time
              Output--> time.struct_time( tm_year=1970, tm_mon=1, tm_mday=1, 
                                          tm_hour=0, tm_min=0, tm_sec=0, 
                                          tm_wday=3, tm_yday=1, tm_isdst=0)
____________________________________________________________________________________________'''
print(f"\nEpoch Time : {T.gmtime(0)}")
# ____________________________________________________________________________________________



'''
Using localtime(seconds)  --> Struct_time formate
                  output --> time.struct_time( tm_year=2023, tm_mon=8, tm_mday=24, 
                                               tm_hour=16, tm_min=41, tm_sec=22, 
                                               tm_wday=3, tm_yday=236, tm_isdst=0)
____________________________________________________________________________________________'''
seconds=T.time()
result=T.localtime(seconds)
print(f"\nThe localtime with (localtime()): {result}")
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
# ____________________________________________________________________________________________






'''
===============================================================================================
______________________________|Seconds|  -->  |String Representation|__________________________
===============================================================================================
-> ctime()


Using ctime(seconds)  --> String representation of time 
                      output--> Thu Aug 24 16:41:20 2023
____________________________________________________________________________________________'''
seconds=T.time()
print(f"\nLocal Time : {T.ctime(seconds)}")
# ____________________________________________________________________________________________










'''
===============================================================================================
______________________________|Struct_time|  -->  |Seconds|__________________________
===============================================================================================
-> mktime()


Using mktime(struct_time)  --> seconds formate
                    output --> 1672197244.0
'''

# struct representation formate
time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
print(f"\nSecond passed (mktime()) : {T.mktime(time_tuple)}")
# ____________________________________________________________________________________________







'''
===============================================================================================
______________________________|Struct_time|  -->  |String Formate|__________________________
===============================================================================================
-> asctime()


Using asctime(struct _time)  -->  String formate of time
                  output     -->   Thu Aug 24 16:41:22 2023
____________________________________________________________________________________________'''
struct_time=T.localtime(T.time())
print(f"\nString Represenattion (asctime) : {T.asctime(struct_time)}")
# ____________________________________________________________________________________________









'''
===============================================================================================
______________________________|Struct_time  |  -->  |String Formate|__________________________
===============================================================================================
______________________________|Formated Code|  -->  |String Formate|__________________________
===============================================================================================
-> strftime()

Using strftime(formated_code)  -->  string form
                output   --> 08/24/2023, 16:41:22

                     struct_time ->  16:41:22
                     
%a -> Short version of Day - Wed
%A -> Full version of Day - Wednesday
%b -> Month name in short version
%B -> Month name in full version
%m -> Month in Digit formate
%y -> Year without century
%Y -> Year with century
%H -> 24 hour formate
%I -> 12 hour formate
%p -> AM/PM
%M -> Minutes
%S -> Seconds

'''
# ____________________________________________________________________________________________
struct_time=T.localtime() 
string_Time = T.strftime("%m/%d/%Y, %H:%M:%S", struct_time)
print("\nFormated Str Representation (strftime) :" ,string_Time)
# ____________________________________________________________________________________________







'''
===============================================================================================
______________________________|  String     |  -->  | Struct_Time|_____________________________
===============================================================================================
______________________________|Fromated Code|  -->  |   String   |_____________________________
===============================================================================================
-> strptime()


Using strptime(string_form)   -->  struct_time
____________________________________________________________________________________________'''
Time_string = "14 July, 2023"
result = T.strptime(Time_string, "%d %B, %Y")
print("\nStruct time : ",result)
# ____________________________________________________________________________________________







'''
===============================================================================================
_______________________________________USe to Delay Execution__________________________________
===============================================================================================
-> sleep()

Using sleep( delay sec)  -->  Dalay of time in seconds
____________________________________________________________________________________________'''
print("\nBefore Sleep -> Hello")
T.sleep(1.5)
print("\nAfter Sleep -> World")
# ____________________________________________________________________________________________
