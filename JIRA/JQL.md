# JQL

**Jira Query Language**

- Jira Issue를 구조적으로 검색 하기 위해 제공하는 언어
- SQL과 비슷
- 쌓인 이슈를 재가공해 유의미한 데이터를 도출하는데 사용

### Operation

- =, !=, >, >=
- in, not in
- ~, !~
- is empty, is not empty, is null, is not null
- AND, OR, NOT ...
- ex)
  project = "DP" and issuetype in (Epic, Story) and created > -2d
