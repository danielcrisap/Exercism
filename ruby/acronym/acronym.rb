class Acronym
  RE_WORD_BOUNDARIES=/\b[a-zA-Z]/.freeze
  def self.abbreviate(phrase)
    phrase.scan(RE_WORD_BOUNDARIES).join.upcase
  end
end