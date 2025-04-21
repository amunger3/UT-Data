-- Average and standard deviation of patients' age by gender
SELECT [PatientGender],
	AVG([PatientAge]) AS AvgAge,
	STDEV([PatientAge]) AS StDevAge
  FROM [Healthcare].[dbo].[DimPatient]
  GROUP BY [PatientGender]

-- Patient and Payer Information (double inner join)
SELECT DISTINCT([Healthcare].[dbo].[DimPatient].[PatientNumber]),
		[FirstName]
      ,[LastName]
      ,[Email]
      ,[PatientGender]
      ,[PatientAge]
      ,[City]
      ,[State]
	  ,[Healthcare].[dbo].[FactTable].[dimPayerPK]
	  ,[Healthcare].[dbo].[DimPayer].[PayerName]
FROM [Healthcare].[dbo].[DimPatient]
INNER JOIN [Healthcare].[dbo].[FactTable]
ON [Healthcare].[dbo].[DimPatient].PatientNumber = [Healthcare].[dbo].[FactTable].PatientNumber
INNER JOIN [Healthcare].[dbo].[DimPayer]
ON [Healthcare].[dbo].[FactTable].[dimPayerPK] = [Healthcare].[dbo].[DimPayer].[dimPayerPK];

-- Physicians by full-time employee status (ProviderFTE == 1 --> full-time employee)
SELECT [dimPhysicianPK]
      ,[ProviderNpi]
      ,[ProviderName]
      ,[ProviderSpecialty]
      ,[ProviderFTE]
  FROM [Healthcare].[dbo].[DimPhyscian]
  ORDER BY [ProviderFTE] DESC;

-- Group patient age and gender by payer
SELECT [Healthcare].[dbo].[DimPatient].[PatientGender]
      ,AVG([PatientAge]) AS AvgAge
	  ,[Healthcare].[dbo].[DimPayer].[PayerName]
FROM [Healthcare].[dbo].[DimPatient]
INNER JOIN [Healthcare].[dbo].[FactTable]
ON [Healthcare].[dbo].[DimPatient].PatientNumber = [Healthcare].[dbo].[FactTable].PatientNumber
INNER JOIN [Healthcare].[dbo].[DimPayer]
ON [Healthcare].[dbo].[FactTable].[dimPayerPK] = [Healthcare].[dbo].[DimPayer].[dimPayerPK]
GROUP BY [Healthcare].[dbo].[DimPatient].[PatientGender], [Healthcare].[dbo].[DimPayer].[PayerName]
ORDER BY AvgAge DESC;