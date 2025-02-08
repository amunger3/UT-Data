# Career Simulation 1 Notes

- Absolutely include a map visual with different data measures (maybe a heatmap).
- No dates in visuals!
- Use Filters or cards for years
- Show top 5 or top 10 (or bottom)
- Seperate State/Federal Table
- For Ranking columns `Rank Sales = RANKX(ALL(Table[Country]), CALCULATE(sum(Table[Sales])))`
- Step 1: Rename to `Workplace_Fatalities`
- Step 2: `FatalitiesPerInspector = DIVIDE('Workplace_Fatalities'[Number of Fatalities, 2012], 'Workplace_Fatalities'[Inspectors],0)`
- Step 3: `InspectorFatalityRank = RANKX(ALL('Workplace_Fatalities'), 'Workplace_Fatalities'[FatalitiesPerInspector],,DESC,Dense)`
- Steps 2 and 3 are calculated in DAX
