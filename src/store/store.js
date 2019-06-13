export const store = {
    _email: '',
    _token: '',

    set email (str) {
      this._email = str
      localStorage.setItem('email',str)
    },
    get email () {
      return this._email || localStorage.getItem('email')
    },

    set token (str) {
      this._token = str
      localStorage.setItem('token',str)
    },
    get token () {
      return this._token || localStorage.getItem('a')
    }

  }