require 'yaml'
require 'find'

# ================================================================================================
# ============================================= UTILS ============================================
# ================================================================================================

$challenges_name = []

Find.find('./challenges') do |path|
  next if File.directory?(path)
  next unless File.basename(path) == 'challenge.yml'

  begin
    challenge = YAML.load_file(path)
    $challenges_name.push(challenge['name'])
  rescue Psych::SyntaxError => e
    next
  end
end

class Validator
  attr_reader :comments
  attr_reader :documentation
  attr_reader :name

  def initialize
    @comments = []
    @name = "#{self.class.name.split(/(?=[A-Z])/).first.downcase} key"
  end

  def validate(value)
  end
end

class CompositeValidator
  def initialize(validators)
    @validators = validators
  end

  def validate(value)
    result = true
    @validators.each do |validator|
      result = validator.validate(value) & result
    end
    result
  end

  def comments
    res = @validators.each_with_object([]) do |validator, acc|
      next if validator.comments.empty?
  
      contents = "<br /> \n <b>:x: #{validator.name}</b>\n\n" +
                 validator.comments.map { |comment| "> #{comment}\n" }.join +
                 <<~EOL

                 <details>
                     <summary>:books: Documentation</summary>
                     #{validator.documentation}
                 </details>
                 EOL
  
      acc << contents
    end.compact

    res
  end
end

class NotEmptyStringValidator < Validator
  attr_reader :key
  attr_reader :default

  def initialize
    super
  end

  def validate(value)
    el = value[@key]

    if el.nil?
      @comments.push("key '#{@key}' not found")
      return false
    end

    if !el.is_a?(String)
      @comments.push("key '#{@key}' should be a string")
      return false
    end

    if el.empty?
      @comments.push("key '#{@key}' shouldn't be empty")
      return false
    end

    if el == @default
      @comments.push("key '#{@key}' shouldn't be equal to '#{@default}' (default value)")
      return false
    end

    true
  end
end

class StringArrayOrEmptyValidator < Validator
  attr_reader :key
  attr_reader :min_elements

  def initialize
    super
  end

  def validate(value)
    is_valid = true
    el = value[@key]

    return true if el.nil? && @min_elements == 0

    unless el.is_a?(Array)
      @comments.push("key '#{@key}' should be an array #{"or empty" if @min_elements == 0}")
      return false
    end

    if el.length < @min_elements
      @comments.push("key '#{@key}' should have at least #{@min_elements} elements")
      return false
    end

    el.each_with_index do |tag, index|
      unless tag.is_a?(String)
        @comments.push("key '#{@key}' element #{index} should be a string")
        is_valid = false
      end
    end

    is_valid
  end
end

def has_depth?(path, desired_depth)
  els = path.split(File::SEPARATOR)
  els.reject!(&:empty?)
  els.length == desired_depth
end


# ================================================================================================
# ========================================== VALIDATORS ==========================================
# ================================================================================================

class StructureValidator < Validator 
  def initialize(path)
    super()
    @documentation = <<~EOL
    \n
    ```
    The structure of the challenge file should be as follow:

    ./challenges
    ├── category [ex: web]
    │   └── challenge [ex: mario_is_missing]
    │       ├── challenge.yml      # obligatory
    │       ├── ...                # optional, files for the challenge
    │       ├── docker-compose.yml # optional, if not present, the challenge does'nt need instance
    │       └── writeup.md         # obligatory
    ```
    EOL

    @path = path
  end

  def validate(value)
    # [ ".", "challenges", "category", "challenge", "callenge.yml" ] (size = 5)
    unless has_depth?(@path, 5)
      @comments.push("your challenge files should be set in ./challenges/[category]/[challenge]/[YOUR_FILES]")
      return false
    end

    true
  end
end

class NameValidator < NotEmptyStringValidator
  def initialize
    super
    @key = 'name'
    @default = 'challenge name'
    @documentation = <<~EOL
    \n
    ```
    The name key represent the name of the challenge on the CTFd platform.

    Constraints:
    - Should be a non-empty string
    - Should be unique

    ex:
    ----------------------------
    name: Mario is missing
    ```
    EOL
  end
end

class AuthorValidator < NotEmptyStringValidator
  def initialize
    super
    @key = 'author'
    @default = 'author'
    @documentation = <<~EOL
    \n
    ```
    The author key represent the name of the author of the challenge.

    This key isn't optional, but you can set it to 'anonymous' if you want to stay anonymous.

    Constraints:
    - Should be a non-empty string

    ex:
    author: anonymous
    ```
    EOL
  end
end

class DescriptionValidator < NotEmptyStringValidator
  def initialize
    super
    @key = 'description'
    @default = 'This is a sample description'
    @documentation = <<~EOL
    \n
    ```
    The description key represent the description of the challenge. 
    It should be written in markdown format (https://www.markdownguide.org/basic-syntax/).

    Constraints:
    - Should be a non-empty string

    ex:
    ----------------------------
    description: |
      This is a drescription 
      of the challenge.
    ```
    EOL
  end
end

class FlagValidator < Validator
  def initialize
    super
    @documentation = <<~EOL
    \n
    ```
    The flag key represent the flag of the challenge. 
    A flag is a string that the user should find to validate the challenge.

    Constraints:
    - Should be an array of string or hash
    - Should have at least one element
    - If it's a string, it should be a non-empty string
    - If it's a hash, it should have a 'type' key and a 'content' key
    - The 'type' key should be 'regex' or 'static'
    - The 'content' key should be a non-empty string

    ex-1 (static flag [case sensitive]):
    ----------------------------
    flags:
      - flag1

    ex-2 (static flag [case insensitive]):
    ----------------------------
    flags:
      - type: static
        content: flag1
        data: case_insensitive

    ex-3 (regex flag [case sensitive]):
    ----------------------------
    flags:
      - type: regex
        content: flag{[a-z]+}
    
    ex-4 (regex flag [case insensitive]):
    ----------------------------
    flags:
      - type: regex
        content: flag{[a-z]+}
        data: case_insensitive
    ```
    EOL
  end

  def validate(value)
    is_valid = true
    flags = value['flags']

    if flags.nil? or !flags.is_a?(Array)
      @comments.push("flags is not an array")
      return false
    end

    flags.each_with_index do |flag, index|
      unless flag.is_a?(String) || (flag.is_a?(Hash) && flag.key?('type') && flag.key?('content'))
        @comments.push("flags[#{index}] is not a string or a hash with 'type' and 'content' keys")
        is_valid = false
      end
    end

    is_valid
  end
end

class TagsValidator < StringArrayOrEmptyValidator
  def initialize 
    super
    @key = 'tags'
    @min_elements = 1
    @documentation = <<~EOL
    \n
    ```
    The tags key represent the tags of the challenge.
    A tag represent a concept that the challenge is related to.

    Constraints:
    - Should be an array of string
    - Should have at least one element
    - Each element should be a non-empty string
    - Each element should be written in lowercase

    ex-1:
    ----------------------------
    tags:
      - web
      - sql

    ex-2:
    ----------------------------
    tags:
      - trivia
    ```
    EOL
  end

  def validate(value)
    is_valid = super
    return false unless is_valid

    tags = value['tags']
    return true if tags.nil?

    tags.each_with_index do |tag, index|
      unless tag.downcase == tag
        @comments.push("tags[#{index}] should be written in lowercase")
        is_valid = false
      end
    end

    is_valid
  end
end

class FilesValidator < StringArrayOrEmptyValidator
  def initialize(path)
    super()
    @key = 'files'
    @min_elements = 0
    @documentation = <<~EOL
    \n
    ```
    The files key represent the files of the challenge.
    A file represent a file that the user should download to solve the challenge.

    If the challenge doesn't have any files, you can omit this key.

    Constraints:
    - Should be an array of string
    - Each element should be a non-empty string
    - Each element should be a path relative to the challenge directory

    ex:
    ----------------------------
    project structure:
    ./challenges
    ├── web
    │   └── mario_is_missing
    │       ├── challenge.yml
    │       ├── file1.txt
    │       ├── file2.txt
    │       └── writeup.md

    challenge.yml:
    ... # other keys
    files:
      - file1.txt
      - file2.txt
    ```
    EOL
    @path = path
  end

  def validate(value)
    is_valid = super
    return false unless is_valid

    files = value['files']
    return true if files.nil?

    dir_path = File.dirname(@path)

    files.each_with_index do |file, index|
      path = File.join(dir_path, file)
      unless File.exist?(path)
        @comments.push("files[#{index}] doesn't exist (#{path})")
        is_valid = false
      end
    end

    is_valid
    
  end
end

class RequirementsValidator < StringArrayOrEmptyValidator
  def initialize 
    super
    @key = 'requirements'
    @min_elements = 0
    @documentation = <<~EOL
    \n
    ```
    The requirements key represent the requirements of the challenge.
    A requirement represent a challenge that the user should have solved before to be able to solve the current challenge.

    If the challenge doesn't have any requirements, you can omit this key.

    Constraints:
    - Should be an array of string
    - Each element should be a non-empty string
    - Each element should be the name of a challenge required by the current challenge

    **important**: The name of the challenge should be the same as the name key of the challenge file.

    ex:
    ----------------------------
    requirements:
      - Mario is missing
    ```
    EOL
  end

  def validate(value)
    is_valid = super
    return false unless is_valid

    requirements = value['requirements']
    return true if requirements.nil?

    requirements.each_with_index do |requirement, index|
      unless $challenges_name.include?(requirement)
        @comments.push("requirements[#{index}] doesn't exist (#{requirement})")
        is_valid = false
      end
    end

    is_valid
  end
end

class WriteupValidator < Validator
  def initialize(path)
    super()
    @name = "#{self.class.name.split(/(?=[A-Z])/).first.downcase} file"
    @documentation = <<~EOL
    \n
    ```
    The writeup file has two purposes:
    - Explain the intended solution of the challenge
    - Has the flag(s) of the challenge

    Constraints:
    - File name should be `writeup.*` (ex: writeup.md, writeup.txt, ...)
    ```
    EOL
    @path = path
  end

  def validate(value)
    dir_path = File.dirname(@path)
    writeup_path = File.join(dir_path, 'writeup.*')

    unless Dir.glob(writeup_path).length == 1
      @comments.push("writeup file not found (#{writeup_path})")
      return false
    end

    true
  end

end


# ================================================================================================
# ========================================== VALIDATION ==========================================
# ================================================================================================
is_valid = true

Find.find('./challenges') do |path|
  next if File.directory?(path)
  next unless File.basename(path) == 'challenge.yml'

  begin
    challenge = YAML.load_file(path)
  rescue Psych::SyntaxError => e
    puts "Challenge '#{path}' is not valid:"
    puts "YAML syntax error: #{e.message}"
    puts
    is_valid = false
    next
  end

  result = CompositeValidator.new([
    StructureValidator.new(path),
    WriteupValidator.new(path),
    NameValidator.new,
    AuthorValidator.new,
    DescriptionValidator.new,
    FlagValidator.new,
    TagsValidator.new,
    FilesValidator.new(path),
    RequirementsValidator.new
  ])

  if !result.validate(challenge)
    puts "### Challenge `#{path}` is not valid"
    print result.comments.join("\n")
    
    is_valid = false
  end
end

exit 1 unless is_valid