class SVReport
  include MongoMapper::Document
  plugin Hunt

  key :id, String
  key :hostmap, String
  key :area, String
  key :submitted, Time

  searches :id, :area
end