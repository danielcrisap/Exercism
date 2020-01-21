module Gigasecond
  GIGASECOND = 10**9

  def self.from(seconds)
    seconds + GIGASECOND
  end
end