Broadcast Adapter Testing Module

This is a software which checks the feed by a broadcaster adapter with internal as well as external references and logs the failures based on certain test cases.
This readme file, explaines how to use this module and in brief the approach in implementation of these test cases.


GUI:



USAGE:

Input Fields:

1. Path to flatfile from Inhouse Adapter: File having inhouse feed for a day
2. Path to flatfile from  Omnesys Adapter: File having omnesys feed for the same day
3. Path to Exchange Bhavcopy: Standard bhavcopy for the day.
4. Path to Lotsize file: This mentions lotsize for all the securities.
5. Time Threshold 1: Logging time durations where omnesys was present but inhouse wasn't (in seconds)
6. Time Threshold 2: Logging time durations where inhouse packets were not present (in seconds)
7. Test modules to be executed: Multiple select allowed

*All the paths should be relative to the .jar file. Or else they can also be absolute. There have been made by default entries there.
Once you have provided all the inputs, press “Start”.

Running:

Once you start the test cases this window will disappear and the code will keep working in background. 
You will see a pop-up when the program ends saying “Program has completed”. 
If there are some errors in between they will also be popped out.
If you want to see the progress, you can open logs/process.log. It will show you the start time, which test cases has started, ended. 

Output:

After completion you can also see the total time taken here
For each individual case(bullet option), there is a separate log folder with names as:
	DB – Depth packet with bhavcopy
	DI – Depth packet with internal reference
	DE – Depth packet with external reference
	LI – LTP with internal reference
	LB – LTP with bhavcopy
Each of these folders have different logs for different test cases, with the first line in each file mentioning the case
There is also *_total.log file in each of these folders which gives the summary of that particular test



IMPLEMENTATION:

Main.java:

This class calls the GUIWindow.java class


GUIWindow.java:

Initializes the entire GUI
The inputs are set to constants.java also in this class
It makes calls to the respective classes for which the radio buttons have been checked one by one


Constants.java:

There is a file “Constants.java” which is more like a 'Control Panel' for this software. It has the following important fields:
String Delimiter="##": Delimiter for both inhouse and omnesys input data
int Index=1: Starting from 0; index in which all the below mentioned fields exist, after splitting
float BThresholdClose =0.99f: Used in LTP Bhav  Test for close price
float BThresholdTotalValue =0.99f: Used in LTP Bhav Test for total value
float BThresholdTotalVolume =0.99f: Used in LTP Bhv Test for total volume/Contracts for the day
long TimeThreshold1: in milliseconds for ONM-INH
, set by user input*1000
long TimeThreshold2: in milliseconds for INH-INH
, set by user input*1000
int LevelSubscribed = 5: No. of levels of market order book
 populated in OMNESYS reference

Below mentioned constants are self-explanatory. They store the index of the field in the input. 
Prefixes:
ID - Inhouse Depth Packet
IL - Inhouse LTP Packet
OD - Omneysys Depth Packet
OL - Omnesys LTP Packet
B - Bhavcopy

	int IDSize = 93;// no. of comma separated fields
	int ILSize = 6;
	int ODSize = 31;
	int OLSize = 4;
	
	*for Lot sizes of different securities
	int LotSymbol = 0;  
	int LotSize = 1;

	int ILSymbol = 0;
	int ILExchangeTime = 1;
	int ILSequenceNumber = 2;
	int ILExchangeEpochTime = 3;
	int ILLTPPrice = 4;
	int ILLTPQuantity = 5;

	int OLSymbol = 0;
	int OLExchangeTime = 1;
	int OLLTPPrice = 2;
	int OLLTPQuantity = 3;

	int IDSymbol = 0;
	int IDTickTime = 1;
	int IDTickDate = 2;
	int IDLTPPrice = 3;
	int IDLTPQuantity = 4;
	int IDTotalBuyQuantity = 5;
	int IDTotalSellQuantity = 6;
	int IDServerTime = 7;
	int IDExchangeTime = 8;
	int IDServerTimeMS = 9;
	int IDExchangeTimeMS = 10;
	int IDSequenceNumber = 11;
	int IDExchangeEpochTime = 12;
	int IDAskPrice = 13;
	int IDAskQuantity = 14;
	int IDBidPrice = 15;
	int IDBidQuantity = 16;
	
	*Below three fields are not being reported as of now, just set the index 	later
	int IDTotalTradedVolume = 5; //dummy
	int IDOpen = 3; //dummy
	int IDClose = 3; //dummy

	int ODSymbol = 0;
	int ODTickTime = 1;
	int ODTickDate = 2;
	int ODLTPPrice = 3;
	int ODLTPQuantity = 4;
	int ODTotalBuyQuantity = 5;
	int ODTotalSellQuantity = 6;
	int ODServerTime = 7;
	int ODExchangeTime = 8;
	int ODServerTimeMS = 9;
	int ODExchangeTimeMS = 10;
	int ODAskPrice = 11;
	int ODAskQuantity = 12;
	int ODBidPrice = 13;
	int ODBidQuantity = 14;

	int BInstrument = 0;
	int BSymbol = 1;
	int BExpiryDate = 2;
	int BStrikePrice = 3;
	int BOptionType = 4;
	int BOpen = 5;
	int BHigh = 6;
	int BLow = 7;
	int BClose = 8;
	int BSettlePrice = 9;
	int BContracts = 10;
	int BValueInLakhs = 11;
	int BOpenInterest = 12;
	int BChangeInOpenInterest = 13;
	int BTimestamp = 14;


DepthInternal.java:


DepthExternal.java:
DepthBhav.java:
LTPInternal.java:
LTPBhav.java:
