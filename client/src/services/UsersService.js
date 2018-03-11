import Api from '@/services/Api'

export default {
  username(username) {
    return Api().get('users/' + username)
  }
}
