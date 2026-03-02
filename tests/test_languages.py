"""Tests for language-specific parsing."""

import pytest
from jcodemunch_mcp.parser import parse_file


JAVASCRIPT_SOURCE = '''
/** Greet a user. */
function greet(name) {
    return `Hello, ${name}!`;
}

class Calculator {
    /** Add two numbers. */
    add(a, b) {
        return a + b;
    }
}

const MAX_RETRY = 5;
'''


def test_parse_javascript():
    """Test JavaScript parsing."""
    symbols = parse_file(JAVASCRIPT_SOURCE, "app.js", "javascript")
    
    # Should have function, class, method, constant
    func = next((s for s in symbols if s.name == "greet"), None)
    assert func is not None
    assert func.kind == "function"
    assert "Greet a user" in func.docstring
    
    cls = next((s for s in symbols if s.name == "Calculator"), None)
    assert cls is not None
    assert cls.kind == "class"
    
    method = next((s for s in symbols if s.name == "add"), None)
    assert method is not None
    assert method.kind == "method"


TYPESCRIPT_SOURCE = '''
interface User {
    name: string;
}

/** Get user by ID. */
function getUser(id: number): User {
    return { name: "Test" };
}

class UserService {
    private users: User[] = [];
    
    @cache()
    findById(id: number): User | undefined {
        return this.users.find(u => u.id === id);
    }
}

type ID = string | number;
'''


def test_parse_typescript():
    """Test TypeScript parsing."""
    symbols = parse_file(TYPESCRIPT_SOURCE, "service.ts", "typescript")
    
    # Should have interface, function, class, method, type alias
    func = next((s for s in symbols if s.name == "getUser"), None)
    assert func is not None
    assert func.kind == "function"
    
    interface = next((s for s in symbols if s.name == "User"), None)
    assert interface is not None
    assert interface.kind == "type"


GO_SOURCE = '''
package main

import "fmt"

// Person represents a person.
type Person struct {
    Name string
}

// Greet prints a greeting.
func (p *Person) Greet() {
    fmt.Println("Hello, " + p.Name)
}

// Add adds two numbers.
func Add(a, b int) int {
    return a + b
}

const MaxCount = 100
'''


def test_parse_go():
    """Test Go parsing."""
    symbols = parse_file(GO_SOURCE, "main.go", "go")
    
    # Should have type, method, function, constant
    person = next((s for s in symbols if s.name == "Person"), None)
    assert person is not None
    assert person.kind == "type"
    
    greet = next((s for s in symbols if s.name == "Greet"), None)
    assert greet is not None
    assert greet.kind == "method"


RUST_SOURCE = '''
/// A user in the system.
pub struct User {
    name: String,
}

impl User {
    /// Create a new user.
    pub fn new(name: &str) -> Self {
        Self { name: name.to_string() }
    }
    
    /// Get the user's name.
    pub fn name(&self) -> &str {
        &self.name
    }
}

pub const MAX_USERS: usize = 1000;
'''


def test_parse_rust():
    """Test Rust parsing."""
    symbols = parse_file(RUST_SOURCE, "user.rs", "rust")
    
    # Should have struct, impl, methods, constant
    user = next((s for s in symbols if s.name == "User"), None)
    assert user is not None
    assert user.kind == "type"


JAVA_SOURCE = '''
/**
 * A simple calculator.
 */
public class Calculator {
    public static final int MAX_VALUE = 100;
    
    /**
     * Add two numbers.
     */
    public int add(int a, int b) {
        return a + b;
    }
}

interface Operable {
    int operate(int a, int b);
}
'''


def test_parse_java():
    """Test Java parsing."""
    symbols = parse_file(JAVA_SOURCE, "Calculator.java", "java")

    # Should have class, method, interface
    calc = next((s for s in symbols if s.name == "Calculator"), None)
    assert calc is not None
    assert calc.kind == "class"

    add = next((s for s in symbols if s.name == "add"), None)
    assert add is not None
    assert add.kind == "method"


PHP_SOURCE = '''<?php

const MAX_RETRIES = 3;

/**
 * Authenticate a user token.
 */
function authenticate(string $token): bool
{
    return strlen($token) > 0;
}

/**
 * Manages user operations.
 */
class UserService
{
    /**
     * Get a user by ID.
     */
    public function getUser(int $userId): array
    {
        return ['id' => $userId];
    }
}

interface Authenticatable
{
    public function authenticate(string $token): bool;
}

trait Timestampable
{
    public function getCreatedAt(): string
    {
        return date(\'Y-m-d\');
    }
}

enum Status
{
    case Active;
    case Inactive;
}
'''


def test_parse_php():
    """Test PHP parsing."""
    symbols = parse_file(PHP_SOURCE, "service.php", "php")

    func = next((s for s in symbols if s.name == "authenticate"), None)
    assert func is not None
    assert func.kind == "function"
    assert "Authenticate a user token" in func.docstring

    cls = next((s for s in symbols if s.name == "UserService"), None)
    assert cls is not None
    assert cls.kind == "class"

    method = next((s for s in symbols if s.name == "getUser"), None)
    assert method is not None
    assert method.kind == "method"
    assert "Get a user by ID" in method.docstring

    interface = next((s for s in symbols if s.name == "Authenticatable"), None)
    assert interface is not None
    assert interface.kind == "type"

    trait = next((s for s in symbols if s.name == "Timestampable"), None)
    assert trait is not None
    assert trait.kind == "type"

    enum = next((s for s in symbols if s.name == "Status"), None)
    assert enum is not None
    assert enum.kind == "type"



SWIFT_SOURCE = '''
import Foundation

let MAX_RETRIES = 3

/// Represents a user model.
struct User {
    let id: Int
    let name: String
}

/// Status of a resource.
enum Status {
    case active
    case inactive
}

/// Handles user operations.
class UserService {
    /// Retrieves a user by id.
    func getUser(userId: Int) -> User? {
        return nil
    }

    /// Creates a new service.
    init(config: String) {
    }
}

extension UserService {
    /// Resets the service state.
    func reset() {
    }
}

protocol Authenticatable {
    func authenticate(token: String) -> Bool
}

/// Authenticate a token.
func authenticate(token: String) -> Bool {
    return !token.isEmpty
}
'''


def test_parse_swift():
    """Test Swift parsing."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")

    const = next((s for s in symbols if s.name == "MAX_RETRIES"), None)
    assert const is not None
    assert const.kind == "constant"

    cls = next((s for s in symbols if s.name == "UserService"), None)
    assert cls is not None
    assert cls.kind == "class"

    method = next((s for s in symbols if s.name == "getUser"), None)
    assert method is not None
    assert method.kind == "method"
    assert "Retrieves a user by id" in method.docstring

    protocol = next((s for s in symbols if s.name == "Authenticatable"), None)
    assert protocol is not None
    assert protocol.kind == "type"

    func = next((s for s in symbols if s.name == "authenticate" and s.kind == "function"), None)
    assert func is not None


def test_parse_swift_struct():
    """Test Swift struct parsed as type."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")
    user = next((s for s in symbols if s.name == "User"), None)
    assert user is not None
    assert user.kind == "type"
    assert "Represents a user model" in user.docstring


def test_parse_swift_enum():
    """Test Swift enum parsed as type."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")
    status = next((s for s in symbols if s.name == "Status"), None)
    assert status is not None
    assert status.kind == "type"
    assert "Status of a resource" in status.docstring


def test_parse_swift_init():
    """Test Swift init declaration parsed as method."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")
    init_sym = next((s for s in symbols if s.name == "init"), None)
    assert init_sym is not None
    assert init_sym.kind == "method"
    assert init_sym.qualified_name == "UserService.init"
    assert "Creates a new service" in init_sym.docstring


def test_parse_swift_extension():
    """Test Swift extension methods are qualified under the extended type."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")

    # Extension itself should NOT appear as a duplicate class symbol
    class_symbols = [s for s in symbols if s.name == "UserService" and s.kind == "class"]
    assert len(class_symbols) == 1

    # Method inside extension should be qualified under the class
    reset = next((s for s in symbols if s.name == "reset"), None)
    assert reset is not None
    assert reset.kind == "method"
    assert reset.qualified_name == "UserService.reset"
    assert "Resets the service state" in reset.docstring


def test_parse_swift_protocol_method():
    """Test Swift protocol method declarations are extracted."""
    symbols = parse_file(SWIFT_SOURCE, "service.swift", "swift")
    proto_method = next(
        (s for s in symbols if s.name == "authenticate" and s.kind == "method"),
        None,
    )
    assert proto_method is not None
    assert proto_method.qualified_name == "Authenticatable.authenticate"
