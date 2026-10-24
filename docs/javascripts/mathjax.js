// MathJax configuration loaded before the MathJax v3 CDN script.
// pymdownx.arithmatex is configured in generic mode in mkdocs.yml.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    packages: { '[+]': ['ams'] }
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  },
  startup: { typeset: true }
};
