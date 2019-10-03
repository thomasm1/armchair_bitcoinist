# 1: Elastic Elasticsearch Service:
### 2019 major upgrade, and launched a slew of new features that enable more use cases and bigger workloads across logging, security, and application data.

### Elastic uses the Google Cloud Platform to help build some of the powerful features that are part of the new Elasticsearch Service, including hot-warm architecture, dedicated master nodes, and machine learning for anomaly detection.

#### Recommended Architecture: 
``SAN attached as block storage, even though SSDs are getting more and more common. Slower storage may not be able to support very high indexing rates, especially when there is also concurrent querying, so it can take a long time to fill up the available disk space. Holding large data volumes per node may therefore only be possible if you have a reasonably long retention period.
```

