import Api from '@/services/Api'

export default {
  signup (credentials) {
    return Api().post('signup', credentials)
  }
}
