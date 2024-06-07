# Feedback manager
## Installation
To install the feedback manager, you can pip install the `viktor-feedback-manager` application. When done, in your
`__init__.py`, add the following line to the imports:

```python
from viktor_feedback_manager import FeedbackManager
from viktor_feedback_manager import Feedback
```

Also, add a root entity to your `InitialEntity`:
```python
InitialEntity('FeedbackManager', name='Feedback Manager')
```

Then, set a secret on the application:
`API_KEY="YOUR_API_KEY"`
Where you should replace `"YOUR_API_KEY"` with a personal access token that has maintainer rights on the application