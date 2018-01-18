import Api from '@/services/Api'

export default {
  index() {
    return Api().get('posts')
  },

  create(post) {
    return Api().post('posts', post)
  }
}
