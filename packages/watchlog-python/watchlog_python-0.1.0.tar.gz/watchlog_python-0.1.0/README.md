# django-watchlog

A python client for [watchlog](https://watchlog.org/) server .

```bash
pip install django-watchlog


## Usage

```python

from django_watchlog import Watchlog

# Create a single instance of Watchlog
watchlog_instance = Watchlog()

# Increment a metric
watchlog_instance.increment('page_views', 10)

# Decrement a metric
watchlog_instance.decrement('items_in_cart', 2)

# Set a gauge metric
watchlog_instance.gauge('current_temperature', 22.5)

# Set a percentage metric
watchlog_instance.percentage('completion_rate', 85)

# Log a system byte metric
watchlog_instance.systembyte('memory_usage', 1024)




```

