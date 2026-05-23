/**
 * 临时存储待上传的文件和需求
 * 用于首页点击启动引擎后立即跳转，在Process页面再进行API调用
 */
import { reactive } from 'vue'

const state = reactive({
  files: [],
  simulationRequirement: '',
  apiKey: '',
  llmBaseUrl: '',
  llmModelName: '',
  isPending: false
})

export function setPendingUpload(files, requirement, apiKey = '', llmBaseUrl = '', llmModelName = '') {
  state.files = files
  state.simulationRequirement = requirement
  state.apiKey = apiKey
  state.llmBaseUrl = llmBaseUrl
  state.llmModelName = llmModelName
  state.isPending = true
}

export function getPendingUpload() {
  return {
    files: state.files,
    simulationRequirement: state.simulationRequirement,
    apiKey: state.apiKey,
    llmBaseUrl: state.llmBaseUrl,
    llmModelName: state.llmModelName,
    isPending: state.isPending
  }
}

export function clearPendingUpload() {
  state.files = []
  state.simulationRequirement = ''
  state.apiKey = ''
  state.llmBaseUrl = ''
  state.llmModelName = ''
  state.isPending = false
}

export default state
