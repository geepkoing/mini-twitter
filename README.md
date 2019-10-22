# mini-twitter-api

## 목표 
- 마이크로 웹 프레임워크 Flask를 통해 미니 트위터 API를 만들면서 백엔드 개발을 전체적으로 정리하기

## 기능
- ping 엔드포인트
- 회원가입
- 로그인
- 트윗
- 다른 회원 팔로우
- 다른 회원 언팔로우
- 타임라인(해당 사용자 및 팔로우한 사용자의 트윗)

## 공부
### 파이썬 가상 환경 
- 해당 프로젝트를 위한 독립된 개발 환경을 만들어 다른 프로젝트와 설정 및 패키지 충돌을 피함
- 콘다 사용법
    - 가상 환경 생성
        - conda create --name api python=3.7 
    - 가상 환경 활성화/비활성화
        - conda activate name api
        - conda deactivate
### 엔드포인트
- API 서버가 제공하는 통신 채널 혹은 접점
- 프론트엔드 서버 등의 클라이언트가 백엔드 API 서버와 통신할 때 엔드포인트에 접속하여 통신
- 개별 엔드포인트는 고유의 URL 주소를 가지며 고유의 기능을 담당하며 이러한 엔드포인트들의 모이면 하나의 API가 됨
- Flask에서는 route 데코레이터를 사용하여 함수들을 엔드포인트로 등록, 즉 엔드포인트 등록은 일반 함수 구현과 마찬가지로 볼 수 있음
### HTTP의 구조 및 핵심 요소   
- HTTP
    - 웹 상에서 서로 다른 서버 사이에 HTML을 주고 받을 수 있도록 만들어진 프로토콜, 통신 규약
    - 웹 기술이 발전하면서 HTML뿐 아니라 다양한 데이터 전송에 사용하게 됨
- HTTP 통신 방식
    - HTTP 요청과 응답
        - HTTP를 기반으로 통신을 할 때 클라이언트가 먼저 HTTP 요청을 보내면 서버는 요청을 처리한 후 결과에 따른 HTTP 응답을 보내는 것으로 하나의 HTTP 통신이 이루어짐
    - stateless
        - HTTP 통신에는 상태(state)라는 개념이 없음, 각 HTTP 통신은 독립적이며 전에 처리된 HTTP 통신에 대해서 전혀 알지 못함
        - HTTP 통신들의 상태를 서버에서 저장할 필요가 없고 각 통신 간의 진행이나 연결 상태의 처리, 저장을 신경쓰지 않아도 되어 서버 디자인이 훨씬 간단해지고 효과적임
        - 단점으로 HTTP 요청을 보낼 때마다 필요한 모든 데이터를 포함시켜서 요청을 보내야 함
            - 쿠키
            - 세션
- HTTP 요청 구조 
    - Start Line
        - HTTP 메소드
            - 해당 HTTP 요청이 의도하는 액션을 정의
            - GET,POST가 주로 쓰임  
        - Request target
            - HTTP 요청이 전송되는 목표 주소 ex) /ping
        - HTTP version
    - Headers
        - HTTP 요청 그 자체의 정보
        - key:value 페어
        - Host
            - target의 호스트 URL 주소
        - User-Agent
            - 요청을 보내는 클라이언트의 정보 ex) 웹 브라우저
        - Accept 
            - 해당 요청이 받을 수 있는 응답 body 데이터 타입을 명시
        - Connection
            - 해당 요청이 끝난 후 클라이언트와 서버가 계속해서 네트워크 연결을 유지할 것인지 끊을 것인지 명시
            - HTTP 통신에서 서버 간 네트워크 연결하는 과정이 다른 작업에 비해 오래 걸리므로 매 요청마다 네트워크 연결을 새로 만드는 것보다 요청이 계속되는 한 재사용을 선호
        - Content-Type
        - Content-Length
    - Body
        - HTTP 요청이 전송하는 데이터를 담는 부분, 전송하는 데이터가 없으면 비어 있음
- HTTP 응답 구조 
    - Status Line
        - HTTP Version
        - Status Code
            - HTTP 응답 상태를 나타내는 미리 지정된 숫자 코드
            - 자주 사용되는 코드 200 OK, 400 Bad Request, 404 Not Found
        - Status Text
            - status code에 대한 부연 설명
    - Headers
    - Body
- API 엔드포인트 아키텍처 패턴
    - API의 엔드포인트 구조를 구현하는 방식
        - RESTful HTTP API
            - API에서 전송하는 리소스를 URI로 표현하고 해당 리소스에 행하려는 의도를 HTTP 메소드로 정의하는 방법
            - 장점
                - 엔드포인트 구조만 봐도 해당 엔드포인트가 제공하는 리소스와 기능을 파악 가능
            - 단점 
                - 클라이언트들이 API가 엔드포인트를 통해 구현해 놓은 틀에 맞추어 사용해야하며 그 틀을 벗어난 사용이 불가능, GraphQL의 등장 이유
        - GraphQL
            - 페이스북이 모바일 앱 개발을 시작하면서 기존 사이트의 API를 재활용하여 모바일 앱을 개발하는 과정에서 어려워 만들게 됨 
            - 엔드포인트가 오직 하나
            - 서버가 정의한 틀에서 클라이언트가 요청하는 것이 아니라 클라이언트가 필요한 것을 서버에 요청하는 방식
## 정리