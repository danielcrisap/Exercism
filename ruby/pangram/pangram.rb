class Pangram
  ALPHABET = ("a".."z")
  def self.pangram?(sentence)
    ALPHABET.all? { |x| sentence.downcase.include?(x) }
  end
end