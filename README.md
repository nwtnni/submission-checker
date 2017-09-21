# submission-checker

Checks if a submission follows the given directory structure, and
provides instant feedback via e-mail.

Written for [Cornell's CS 2112](http://www.cs.cornell.edu/courses/cs2112/2017fa/) 
using the [CMS autograder API](http://www.cs.cornell.edu/Projects/cms/userdoc/autograder.html). 

## Documentation

`server.py` launches a [Flask](http://flask.pocoo.org/) web server that 
can hook into [CMS](http://www.cs.cornell.edu/Projects/cms/) submissions.
CMS sends a POST request to the server with data for each submission,
([documented in the autograder API](http://www.cs.cornell.edu/Projects/cms/userdoc/autograder.html)).

Each assignment with name `<ASSIGNMENT_NAME>` should have a corresponding
text file `<ASSIGNMENT_NAME>.txt` in the `requirements` directory. This
file defines a whitelist for directories and files in the student submission.
Here's an example template:

```
src
readme.txt
problems.pdf
src/util
src/util/Example.java
src/test
src/test/ExampleTest.java
```

Any missing files from this reference, and any extra files, are logged and
sent to the student's Cornell netID e-mail. For the purposes of this course,
extra `.java` files are not logged.
