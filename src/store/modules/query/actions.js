import queryService from '@/services/queryService'

const QUERY_DATABASE = async (context, payload) => {
  let tempArray = []
  let data = await queryService.postFileNames({query: payload})
  let temp = JSON.parse(data)
  temp.data.forEach(x => {
    tempArray.push(x.filename)
  })
  return tempArray
}

export default {
  QUERY_DATABASE
}
