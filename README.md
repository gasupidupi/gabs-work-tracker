# gabs-work-tracker
CLI tool to track what you work on for how long, so you'll have an easier time registering your work in whatever annoying tool your manager wants you to use but you can only mentally handle to log in once he breaths down your neck about it.

# installation
1. Set the output directory for the tracker log in tracker/config.yml.
2. Install using:
```
pip install .
```

# usage
### Change output directory for tracker log
```
tracker config --o path/to/desired/output/dir
```
### Add message and ticket number at the end of session
```
tracker track
```
### Or add them at the start
```
tracker track --m "Security upgrade" --t "EG-123"
```
### Use the past option to use the last end time as your start time
```
tracker track --m "Security upgrade" --t "EG-123" --p
```
### Delete log
```
tracker clear
```
### Show log
```
tracker show
```
#### Example output
```
24/08/2025   08:00   09:00   EG-001   Security upgrade

24/08/2025   09:00   10:00      Daily meeting

24/08/2025   10:00   12:00   EG-002   Wrote tests for hello world functionality
```
