# UT Data Notes

## 1/15

- 70% Lecture Attendance required
- Office Hours - 9am to 6pm CST (M-F)
- Don't skip videos
- "Coaching" Tab - schedule a 1-on-1
- PROJECTS - MADATORY ON TIME
- Surveys also mandatory
- 855-800-8224 Help Desk M-F 9-6 CST (10-7 EST)

## 1/18

- Just talking about class mostly
- No technical talk
- [4 Pillars of Data Science](https://towardsdatascience.com/the-four-pillars-of-a-data-career-d6a09edf8ac9)
- AI helper ([Claude](https://claude.ai/) the best for reliability of answers.)
- All clases will be uploaded under the fileshare tab

## 1/22

### Start of Excel Unit

- Need to actually get Excel somehow
- Perhaps for now Google Sheets will suffice
- For now using Excel on Danna's Mac.
- Need to pull Git to it
- [Excel Licenses (GroupOn)](https://www.groupon.com/deals/license-tom-llc-1)

### PowerBI

- Downloaded
- Not sure about license

## 1/25

### Excel Unit

- Using Danna's computer for Excel
- Got PowerBI working

## 1/29

### Excel Unit Continued

- On Job Search: Advice "Stay away from DBA"
- Indeed, LinkedIn, SimplyHired (?), Google
- Use AI to "spruce up" your resume
- Projects are just pass/fail

## 2/1

### Resume Help

- Reach out to Advisor

### PowerBI continued

- [Matrix Visuals](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual?tabs=powerbi-desktop)
- [Paginated Reports](https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi)
- For changing a complex table for sandbox, click "duplicate table".
- [Dax Functions](https://dax.guide/functions/)

## 2/5

- Do the project in PowerBI
- Everything is "how you interpret the data".
- Ignore "Excel Report" in project guidelines and you can instead upload a PowerBI file.
- This is your dataset, no wrong or right answers, just focused on providing deliverables and "how your mind works".

## 2/8

- PowerBI `DENSE_RANK` guarantees tie-breaks and doesn't skip ranks.

## 2/12

- `Avg Penalty per Inspector = DIVIDE(SUM('2012_Workplace_Fatalities_by_State'[Penalties FY 2013 (Average $)]),SUM('2012_Workplace_Fatalities_by_State'[Inspectors]),0)`
- `if(inspector="", 0, 1/2)`
- `if(isblank(inspect) || value 0, 0, 1/2)`
- Let me help you troubleshoot this issue. Several common causes can make Power BI show blank data during transformation. - Let's go through the potential solutions:
    Check Source Data Connection
    Verify the data source is still accessible
    Refresh your credentials if needed
    Test the connection in the Power BI "Data Source Settings"
    Column Headers
    If headers were improperly detected:
    Go to "Transform" tab
    Click "Use First Row as Headers"
    If already selected, try "Remove Top Rows" and then set headers again
    Data Type Issues
    Check if Power BI correctly identified data types
    In Power Query Editor:
    Right-click column headers
    Select "Change Type"
    Manually set correct data types
    Clear Cache and Refresh
    In Power BI:
    File → Options and Settings → Options
    Current File → Data Load
    Click "Clear Cache"
    Then refresh your data
    Query Steps Check
    Open Power Query Editor
    Review Applied Steps on the right
    Look for steps that might be filtering out data
    Try removing and re-adding problematic steps
- Next 3 weeks: PowerBI

## 2/15

- Real-world stuff next week
- Calculated columns (row-by-row) (any table)
- Calculated measures
- We haven't touched the word Swift yet?
- [DAX Practice Site](https://dax.do/)
- [DAX Guide](https://dax.guide/)

## 2/19

- ToastMasters (classes) for public speaking
- Put your best resume together and throw it at companies
- Other job website - "PostJobFree"

## 2/22

- Python soon, maybe figure out a [conda](https://www.anaconda.com/download) distro
- Another link to explore, [hex.tech](https://hex.tech/)
- Going back to PowerBI sample dataset
- Making a PowerBI Dashboard with Cohort Data Set

## 2/26

- PowerBI today, 3/5 is SQL
- Next project is combination of PowerBI and SQL
- `YearMonth = FORMAT(Plans[Datekey], "yyyymm")`
- `discount = IF( and( Plans[YearMonth] >= 200701, Plans[YearMonth] <= 200706), Plans[PricePerItem] * 0.45, IF( and( Plans[YearMonth] >= 200707, Plans[YearMonth] <= 200712), Plans[PricePerItem] * 0.35, IF( and( Plans[YearMonth] >= 200801, Plans[YearMonth] <= 200810), Plans[PricePerItem] * 0.25,IF( and( Plans[YearMonth] >= 200811, Plans[YearMonth] <= 200812), Plans[PricePerItem] * 0.08,IF( and( Plans[YearMonth] >= 200904, Plans[YearMonth] <= 200908), Plans[PricePerItem] * 0.60, IF( and( Plans[YearMonth] >= 200912, Plans[YearMonth] <= 200912), Plans[PricePerItem] * 0.75,  0))))))`

```Discounted Price =
VAR CurrentYear = [Year]
VAR CurrentMonth = [Month]
VAR OriginalPrice = [PricePerItem]
RETURN
    SWITCH(
        TRUE(),
        -- 45% discount for 2007, months 1-6
        CurrentYear = 2007 && CurrentMonth >= 1 && CurrentMonth <= 6,
        OriginalPrice * 0.45,  -- 100% - 45% = 55%
        
        -- 35% discount for 2007, months 7-12
        CurrentYear = 2007 && CurrentMonth >= 7 && CurrentMonth <= 12,
        OriginalPrice * 0.35,  -- 100% - 35% = 65%
        
        -- 25% discount for 2008, months 1-10
        CurrentYear = 2008 && CurrentMonth >= 1 && CurrentMonth <= 10,
        OriginalPrice * 0.25,  -- 100% - 25% = 75%
        
        -- 8% discount for 2008, months 11-12
        CurrentYear = 2008 && CurrentMonth >= 11 && CurrentMonth <= 12,
        OriginalPrice * 0.08,  -- 100% - 8% = 92%
        
        -- 60% discount for 2009, months 4-8
        CurrentYear = 2009 && CurrentMonth >= 4 && CurrentMonth <= 8,
        OriginalPrice * .60,   -- 100% - 60% = 40%
        
        -- 75% discount for 2009, month 12 only
        CurrentYear = 2009 && CurrentMonth = 12,
        OriginalPrice * 0.75,  -- 100% - 75% = 25%
        
        -- Default: no discount
        OriginalPrice
    )
```

- Add AI skills to resume
- PowerBI Quiz in class Saturday

## 3/1

- **Jeff Email**: [jeff.lund@quickstart.com](mailto:jeff.lund@gmail.com)
- **Jeff Calendar appointment**: [Appointment](https://calendly.com/jeff-lund/datascience)
- Installed SQL Server and Tools for next week

## 3/5

- There is supposed to be an SQL module that I cannot see yet (hopefully resolved by Saturday)
- SQL course starts 3/12
- Some sort of assessment on Saturday?
- PowerBI today, SQL Saturday 3/8
- One extra day of SQL, one extra day of PowerBI
- [Microsoft Copilot Article](https://www.techtarget.com/searchdatamanagement/tip/How-to-use-Microsoft-Copilot-in-Power-BI)

## 3/8

- SQL start
- My Management studio is saved at "C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE\Ssms.exe"
- Cars database should be properly loaded and I have saved a couple of queries including an example view
- Data Analysts usually cannot manipulate a table directly but can query and save their own view for manipulation

## 3/12

- Some notes for the Cars database:
- To query the whole table: `SELECT * FROM Cars.dbo.Car_sales`
- Rememeber `ASC` (Ascending) is default result order when using an `ORDER BY` clause
- More queries stored [here]('C:\Users\munge\OneDrive\Documents\SQL Server Management Studio')
- To "use" a database for a set of queries: `USE db_name GO`
- You must use a `GROUP BY` anytime you have an aggregated command
- Correlation coefficient in SQL [here](https://chartio.com/learn/postgresql/correlation-coefficient-pearson/)
- `COUNT(*)` selects all the columns
- Quiz on Saturday, work a little more on understanding correlation coefficient in SQL

## 3/15

- Begin work on the Baseball database
- Loaded database from a shared file called 'Baseball.bak'
- SQL Server Management Studio should have it loaded, [here](./Example-Files/Baseball.bak)

## 3/19

- Missed class. Catch up with notes later.

## 3/22

- Career Simulation 2 dicussion
- PowerBI requirements: 3 pages, 3 visuals per page, 2 slicers per page
- Will use vegetable sales dataset
- Started on SQL Queries -- need to finish early this week

## 3/26

- Submitted Career Simulation 2
- Microsoft Fabric Start
- Chat Note:
    `YoY % Change = VAR CurrentYear = [Total Sales] VAR PreviousYear = CALCULATE([Total Sales], DATEADD(Dates[Date], -1, YEAR)) RETURN IF(PreviousYear <> 0, DIVIDE(CurrentYear - PreviousYear, PreviousYear), BLANK())`
- Need to somehow "signup with a work email" to download 60 day trial of Microsoft Fabric
- [Microsoft Fabric Web](https://app.fabric.microsoft.com/home?culture=en-us&country=us&experience=fabric-developer)
- Microsoft account: [dayana.quintanilla@chattacademy.org](mailto:dayana.quintanilla@chattacademy.org) Egnwse314!

## 3/29

- More Microsoft Fabric
- Discussing importing data into PowerBI and issues
- One more week on Fabric
- Then another project (still PowerBI)
- Then move into Python
- Questions:
- *True or False*: Power BI Desktop can connect directly to an on-premises SQL Server database without any additional configuration. False. It needs to be configured.
- *True or False*: In Power BI, you can create calculated columns in both Power Query Editor and Data View. False, only in Query Editor.
- *True or False*: Row-level security (RLS) in Power BI can be implemented directly in the Power BI Service without setting it up in Power BI Desktop first.
- *True or False*: Power BI Premium capacity allows for larger dataset sizes compared to Power BI Pro. True. Power BI Premium supports larger dataset sizes, currently up to 50 GB compared to 1 GB in Power BI Pro.
- *True or False*: When using Direct Query, all data transformations must be done at the source before connecting to Power BI. True.
- Which of the following storage modes is NOT available in Power BI? (A) Import (B) DirectQuery (C) Composite (D) Remote. Answer: (D) Remote. You cannot store data remotely.
- Which of the following visuals has built-in drill-down functionality by default? (A) Table (B) Matrix (C) Pie Chart (D) Gauge *(B) Matrix*
- What is the primary purpose of using a Parameter in Power Query? (A) To create DAX measures (B) To dynamically change data sources or query elements (C) To format visuals (D) To implement row-level security *(B) To dynamically change data sources or query elements*
- In Power BI, the *Model* view is where you create relationships between tables.
- The *web connector* connector in Power BI allows you to connect to various websites and extract table data.
- When you need to combine tables with the same schema, you should use the *append* operation in Power Query.
- Which of the following is NOT a valid data category for column formatting in Power BI? (A) Web URL (B) Country/Region (C) Database Name (D) Image URL *(C) Database Name*
- A Sankey diagram (referenced in question #48) is a specialized visualization type in Power BI that shows flows between categories by using connecting bands or ribbons. The width of these bands represents the magnitude of the flow between nodes.
- The *Performance Analyzer* diagnostic tool in Power BI Desktop helps identify performance bottlenecks in reports.

## 4/2

- [Power BI Transitions](https://www.plainconcepts.com/transition-power-bi-fabric/)
- [Transitionin from PowerBI to Fabric](https://powerbi.microsoft.com/en-us/blog/grace-period-for-transitioning-from-power-bi-premium-to-microsoft-fabric/)
- [Microsoft On-Premises Data Gateway](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install)

## 4/5

- [Learning Microsoft Fabric (Main Page)](https://www.skool.com/microsoft-fabric)
- [Learning Microsoft Fabric (Videos)](https://www.youtube.com/@LearnMicrosoftFabric)
- [Data Witches - M365 Developer License](https://data-witches.com/2023/01/m365-developer-license-fabric/)
- [End-to-End Tutorials in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/end-to-end-tutorials)
- [Signing up for Office 365 Video](./References/Power%20BI/PowerBI.mp4)
- Most useful programs/languages for this field: know PowerBI, Python, and SQL

## 4/9

- Get data from [Kaggle](https://www.kaggle.com/search)
- Get a primary and a backup dataset
- Health, Medical Insurance, fields like this
- Project Due: *April 22* (no extensions)
- Interesting project, but only one table: [Data Analysis](https://www.kaggle.com/code/manarmohamed24/analysis-healthcare-dataset)
- Search for a multi-table dataset for SQL use
- Possiblities:
- [Health Care Analytics](https://www.kaggle.com/datasets/abisheksudarshan/health-care-analytics)
- [Option 2](https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey)
- [Option 3](https://app.gigasheet.com/spreadsheet/healthcare-dataset/d06ad9e5_09cb_43c6_9dec_3af364aa8e46?_gl=1*12pici6*_gcl_au*MTEzMDQ4NTU3NS4xNzQ0MjQzODMy)
- [Option 4](https://mavenanalytics.io/data-playground?order=date_added%2Cdesc&search=health)
- [Doing this one](https://www.kaggle.com/datasets/tomaslui/healthcare-dataset)

## 4/12

- Data (CSVs) put into Final-Career-Simulation folder
- Need to work on project this week
- Class is just fielding questions about the project
- Long discussion with Catlan and Mohammed [msher4ai@gmail.com](mailto:msher4ai@gmail.com) about Python

## 4/16

- Need to get project done this weekend
- All tables created in SQL Server

## 4/19

- All tables loaded into PowerBI
- Python practice all class
- Loaded tables into Python, no analysis done

## 4/23

- Project finished and turned in
- Did a bunch of work in Python (see [here](./Python-Files/))

## 4/26

- Shared documents (In [PDF](./Instructor-Shares/PDF/)) about seeking a career as a PowerBI Analyst

## 4/30

- Met with Kevin before class (see [Notes](./Career/Career.md))
- More Python and Jupyter

## 5/3

- Have resume review session on 5/5 @ 4:30
- Python ML debug session (ml_basic_to_students file)

## 5/10

- More Python

## 5/14

- Last class is 5/24 due to schedule change
- PowerBI test on-site or at home (monitored) -- 30-60 questions
- Certificates nice "to get foot in the door" -- after that experience
- Jeff has zero certificates, for example

## 5/17

- Python certificate talk

## 5/21

- Preparing for PowerBI Certificate Exam - see other specific notes [here](./Career/PowerBI-Cert.md)
- PowerBI and Python (TOGETHER) Saturday!! *Last Class*
