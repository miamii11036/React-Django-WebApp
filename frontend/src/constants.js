/*作為攔截器，會攔截我們傳送的任何request，並自動新增header */
import axios from 'axios'; //會檢查每一個傳送的request是否有token，如果有就會自動加上header