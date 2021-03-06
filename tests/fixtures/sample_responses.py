METRIC_DATA_SAMPLE = """
<?xml version="1.0" encoding="UTF-8"?>
<metrics type="array">
  <metric app="My Application" agent_id="123456" begin="2011-04-20T15:47:00Z" end="2011-04-20T15:48:00Z" name="ActiveRecord/all">
    <field type="integer" name="average_response_time">0</field>
  </metric>
  <metric app="My Application" agent_id="123456" begin="2011-04-20T15:48:00Z" end="2011-04-20T15:49:00Z" name="ActiveRecord/all">
    <field type="integer" name="average_response_time">0</field>
  </metric>
  <metric app="My Application" agent_id="123456" begin="2011-04-20T15:49:00Z" end="2011-04-20T15:50:00Z" name="ActiveRecord/all">
    <field type="integer" name="average_response_time">0</field>
  </metric>
  <metric app="My Application" agent_id="123456" begin="2011-04-20T15:50:00Z" end="2011-04-20T15:51:00Z" name="ActiveRecord/all">
    <field type="integer" name="average_response_time">0</field>
  </metric>
  <metric app="My Application" agent_id="123456" begin="2011-04-20T15:51:00Z" end="2011-04-20T15:52:00Z" name="ActiveRecord/all">
    <field type="integer" name="average_response_time">0</field>
  </metric>
</metrics>
"""

METRIC_NAMES_SAMPLE = """
<?xml version="1.0" encoding="UTF-8"?>
<metrics type="array">
  <metric name="WebTransaction">
    <fields type="array">
      <field name="average_call_time"/>
      <field name="average_response_time"/>
      <field name="call_count"/>
      <field name="max_call_time"/>
      <field name="min_call_time"/>
      <field name="requests_per_minute"/>
      <field name="throughput"/>
      <field name="total_call_time"/>
    </fields>
  </metric>
  <metric name="WebTransaction/RPMCollector/AgentListener/connect">
    <fields type="array">
      <field name="average_call_time"/>
      <field name="average_response_time"/>
      <field name="call_count"/>
      <field name="max_call_time"/>
      <field name="min_call_time"/>
      <field name="requests_per_minute"/>
      <field name="throughput"/>
      <field name="total_call_time"/>
    </fields>
  </metric>
</metrics>
"""

VIEW_APPLICATIONS_SAMPLE = """
<?xml version="1.0" encoding="UTF-8"?>
<applications type="array">
  <application>
    <id type="integer">123</id>
    <name>My Application</name>
    <overview-url>https://rpm.newrelic.com/accounts/1/applications/123</overview-url>
    <servers-url>https://api.newrelic.com/api/v1/accounts/1/applications/123/servers</servers-url>
  </application>
  <application>
    <id type="integer">124</id>
    <name>My Application2</name>
    <overview-url>https://rpm.newrelic.com/accounts/1/applications/124</overview-url>
    <servers-url>https://api.newrelic.com/api/v1/accounts/1/applications/123/servers</servers-url>
  </application>
</applications>
"""

THRESHOLD_VALUES_SAMPLE = """
<?xml version="1.0" encoding="UTF-8"?>
<threshold-values type="array">
  <threshold_value name="Apdex" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="0.96 [1.0]*" threshold_value="1" metric_value="0.96"/>
  <threshold_value name="Application Busy" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="3%" threshold_value="1" metric_value="3"/>
  <threshold_value name="CPU" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="52.86 %" threshold_value="1" metric_value="52.86"/>
  <threshold_value name="Memory" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="261.42 MB" threshold_value="1" metric_value="261.42"/>
  <threshold_value name="Errors" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="0.0 epm" threshold_value="1" metric_value="0.0"/>
  <threshold_value name="Response Time" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="31 ms" threshold_value="1" metric_value="31"/>
  <threshold_value name="Throughput" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="14028.6 cpm" threshold_value="1" metric_value="14028.6"/>
  <threshold_value name="DB" begin_time="Fri Dec 12 01:22:00 +0000 2008" end_time="Fri Dec 12 01:27:00 +0000 2008" formatted_metric_value="46.82 %" threshold_value="1" metric_value="46.82"/>
</threshold-values>
"""

DELETE_APPLICATION_SUCCESS_SAMPLE = """
<?xml version="1.0" encoding="UTF-8"?>
<applications type="array">
  <application name="MyApp" id="1234">
    <result>deleted</result>
  </application>
  <application name="MyApp 2" id="2345">
    <result>failed</result>
  </application>
</applications>
"""