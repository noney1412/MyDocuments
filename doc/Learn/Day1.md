---
styled-components

- primary : css` font-size:15`

switch to learn react router*
--> concern about SEO [SPA**]
:: SPA VS MPA : https://medium.com/@NeotericEU/single-page-application-vs-multiple-page-application-2591588efe58

:: SPA optimize for SEO :
http://blog.rapidapi.com/2017/01/24/optimizing-seo-for-single-page-applications-with-isomorphic-javascript/


```
SEO
ประเด็นนี้สำคัญสุดๆ ครับ เพราะว่าเว็บแบบ SPA นั้น ไม่ค่อยดีต่อ SEO เท่าไร (จริงๆ ก็ทำให้ดีได้ แต่ค่อนข้างจะลำบาก) แต่ Isomorphic นั้นได้ SEO ไปเต็มๆ ครับ เพราะ server จะ render หน้าที่มีข้อมูลสมบูรณ์มาให้ตั้งแต่ตอนที่โหลดมาครั้งแรกแล้ว

http://www.siamhtml.com/build-isomorphic-apps-with-react/
```

--> หาวิธีเขียน Server Side Render 

:client: ---> Request                   ---> :server:
:client: <--- Fully Rendered HTML Page  <--- :server:
:client: ---> Ajax Request              ---> :server:
:client: <--- JSON response             <--- :server:

```
React-Router (https://www.npmjs.com/package/react-router): This is a must-have library for working with routes. The most interesting part of this library for isomorphic apps is the match function. The match function matches a set of routes to a location without rendering, and calls a callback when it’s done. That means that you don’t need to write the routing twice (once for backend, once for frontend).

docs: https://knowbody.github.io/react-router-docs/
```
Isomophic Application:
https://www.babelcoder.com/blog/posts/react-redux-isomorphic-day4-react-redux-isomorphic

---
