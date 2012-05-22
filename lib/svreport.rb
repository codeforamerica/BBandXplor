class SVReport
  include MongoMapper::Document
  plugin Hunt

  key :id, String
  key :hostmap, String
  key :area, String
  key :submitted, Time
  key :response, Array
  key :latlng, Array

  searches :id, :area, :hostmap
end