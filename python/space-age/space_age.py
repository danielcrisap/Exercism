class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years_seconds = 365.25*24*60*60

    def on_earth(self):
        orbital_period = 1
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_mercury(self):
        orbital_period = 0.2408467
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_venus(self):
        orbital_period = 0.61519726
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_mars(self):
        orbital_period = 1.8808158
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_jupiter(self):
        orbital_period = 11.862615
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_saturn(self):
        orbital_period = 29.447498
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_uranus(self):
        orbital_period = 84.016846
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)

    def on_neptune(self):
        orbital_period = 164.79132
        years = self.seconds/(self.earth_years_seconds * orbital_period)
        return round(years, 2)
