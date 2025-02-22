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
