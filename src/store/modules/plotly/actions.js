import previewService from '@/services/previewService'

const GET_PREVIEW_SOURCES = async (context, payload) => {
  let data = await previewService.getValueCounter(payload)
  if (data) {
    let stack = await previewService.getStack(payload)
    let multipleLines = await previewService.getMultipleLines(payload)

    context.commit("SET_STACKED", JSON.parse(stack))
    context.commit("SET_MULTIPLE_LINES", JSON.parse(multipleLines))
    context.commit("SET_PREVIEW_SOURCES", JSON.parse(data))
    return 200
  } else {
    context.commit("DEFAULT_PREVIEW_STATES")
    return 404
  }
}

export default {
  GET_PREVIEW_SOURCES
}
