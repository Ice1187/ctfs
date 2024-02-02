From the doc:

> To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), preferring an exact match but **also accepting a case-insensitive match**.

```
curl https://point.mc.ax -d '{"What_point": "that_point"}'
```
