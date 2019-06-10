const updateToken = (state, newToken) => {
  localStorage.setItem('t', newToken);
  state.jwt = newToken;
}
const removeToken = (state) => {
  localStorage.removeItem('t');
  state.jwt = null;
}

export default {
  updateToken,
  removeToken
};
