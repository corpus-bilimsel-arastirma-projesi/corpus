import previewService from '@/services/previewService'

const POST_PREVIEW_SOURCES = async (context, payload) => {
  let data = await previewService.postPreviewSources({uuid: payload})
  if (data) {
    let wordCloud = []
    let verticalBar = []
    let verticalBarCategories = []
    for (let [key, value] of Object.entries(data)) {
      wordCloud.push({
        name: key,
        weight: parseInt(value)
      })

      verticalBar.push({
        name: key,
        color: '#1976D2',
        y: parseInt(value)
      })

      verticalBarCategories.push(key)
    }

    context.commit("SET_PREVIEW_WORD_CLOUD", wordCloud)
    context.commit("SET_PREVIEW_VERTICAL_BAR", verticalBar)
    context.commit("SET_PREVIEW_VERTICAL_BAR_CATEGORIES", verticalBarCategories)
    return 200
  } else {
    context.commit("DEFAULT_PREVIEW_STATES")
    return 404
  }
}

export default {
  POST_PREVIEW_SOURCES
}
