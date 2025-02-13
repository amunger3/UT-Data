# 2/12 Notes

- 2/12 Notes
- Avg Penalty per Inspector = DIVIDE(SUM('2012_Workplace_Fatalities_by_State'[Penalties FY 2013 (Average $)]),SUM('2012_Workplace_Fatalities_by_State'[Inspectors]),0)
- if(inspector="", 0, 1/2)
- if(isblank(inspect) || value 0, 0, 1/2)
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