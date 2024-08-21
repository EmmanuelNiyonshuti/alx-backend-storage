-- list all bands with Glam rock as their main style, ranked by their longevity.
-- Lifespan is calculated as the difference between the year (2022) and the formed year.
-- If the split year is present, use it; otherwise, use 2022 as the end year.

SELECT 
    band_name, COALESCE(split, 2022) - formed AS lifespan
FROM
    metal_bands
WHERE
    style = "Glam rock"
ORDER BY
    lifespan DESC;
