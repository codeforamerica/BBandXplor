class ProcessSVReport
  def self.perform(params)
    //document = SVReport.find!(params["id"])
    
    document = SVReport.create({
      :submitted => Time.now(),
      :hostmap => "broadband3",
      :area => params["area"],
      :latlng => [ params["lat"], params["lng"] ]
    })

    #pdf = document.pdf

    #if pdf.grim.count > 0
    #  document.preview = File.open(pdf.create_preview)

    #  pdf.grim.each do |page|
    #    document.page_contents << page.text
    #  end

    #  document.save!
    #else
    #  raise 'PDF has no content'
    #end
    #document.save!
  end
end