import previewService from '@/services/previewService'

const POST_PREVIEW_SOURCES = async (context, payload) => {
  let data = await previewService.postPreviewSources({uuid: payload})
  if (data) {
    let wordCloud = []
    let verticalBar = []
    for (let [key, value] of Object.entries(data)) {
      console.log(`${key}: ${value}`)

      wordCloud.push({
        text: key,
        weight: parseInt(value),
        rotation: 1,
        rotationUnit: 'turn',
        fontFamily: 'Anton',
        fontStyle: 'normal', // normal|italic|oblique|initial|inherit
        fontVariant: 'normal', // normal|small-caps|initial|inherit
        fontWeight: 'normal', // normal|bold|bolder|lighter|number|initial|inherit
        color: '#' + (Math.random().toString(16) + "000000").substring(2, 8)
      })
      verticalBar.push({key: key, value: parseInt(value)})
    }

    context.commit("SET_PREVIEW_WORD_CLOUD", wordCloud)
    context.commit("SET_PREVIEW_VERTICAL_BAR", verticalBar)
    return 200
  } else {
    context.commit("DEFAULT_PREVIEW_STATES")
    return 404
  }
}

export default {
  POST_PREVIEW_SOURCES
}
