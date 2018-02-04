import Api from '@/services/Api'

export default {
  create(post) {
    return Api().post('subvues', post)
  }
}
