import request from '@/utils/request'
// /vue-element-admin-i18n/src/utils/request.js 这里面有个import axios
// axios.create    baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
export function login(data) {
  return request({
    url: '/vue-element-admin/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/vue-element-admin/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-element-admin/user/logout',
    method: 'post'
  })
}
