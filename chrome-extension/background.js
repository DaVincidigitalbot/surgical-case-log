// ============================================================
// Clinical Case Log → ACGME Export — Background Service Worker
// ============================================================

// Listen for messages from content script
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === 'GET_PENDING_EXPORT') {
    chrome.storage.local.get(['pendingExport', 'exportTimestamp'], (data) => {
      // Only return if export was set within last 5 minutes
      if (data.pendingExport && data.exportTimestamp && (Date.now() - data.exportTimestamp < 300000)) {
        sendResponse({ cases: data.pendingExport });
        // Clear after delivery
        chrome.storage.local.remove(['pendingExport', 'exportTimestamp']);
      } else {
        sendResponse({ cases: [] });
      }
    });
    return true; // async response
  }
});

// Badge to show pending export count
chrome.storage.onChanged.addListener((changes) => {
  if (changes.pendingExport) {
    const cases = changes.pendingExport.newValue;
    if (cases && cases.length > 0) {
      chrome.action.setBadgeText({ text: String(cases.length) });
      chrome.action.setBadgeBackgroundColor({ color: '#2EA8FF' });
    } else {
      chrome.action.setBadgeText({ text: '' });
    }
  }
});
